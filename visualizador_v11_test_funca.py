# srt_monitor.py — Visor SRT con Flask, refresh cada 10 min
from flask import Flask, render_template_string
import pandas as pd, time

app = Flask(__name__)
CSV = "CSV_FILES\\SRT_consolidados.csv"   # ← ruta al archivo CSV (relativa o absoluta)

TMPL = """<!DOCTYPE html><html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="600">  <!-- recarga la página cada 600 s = 10 min -->
  <title>SRT Monitor</title>
  <style>
    body{font-family:Arial;font-size:12px;background:#0d1b2a;color:#e0e0e0;margin:0;padding:10px}
    h1{color:#4cc9f0;text-align:center;margin:8px 0}
    .info{text-align:center;color:#aaa;margin-bottom:8px}
    .stats{display:flex;justify-content:center;gap:16px;margin-bottom:12px}
    .stat{background:#16213e;padding:6px 18px;border-radius:8px;text-align:center}
    .stat b{font-size:22px;display:block}
    table{width:100%;border-collapse:collapse;display:block;overflow-x:auto}
    th{background:#1a3a5c;color:#4cc9f0;padding:6px 8px;border:1px solid #2d4a6e;
       position:sticky;top:0;white-space:nowrap;z-index:1}
    td{padding:4px 8px;border:1px solid #1e3a5f;white-space:nowrap}
    tr:nth-child(even){background:#0f2540} tr:hover{background:#1e4080}
    .ok{color:#06d6a0;font-weight:bold}   /* connected     → verde  */
    .err{color:#ef476f;font-weight:bold}  /* disconnected  → rojo   */
    .warn{color:#ffd166;font-weight:bold} /* connecting    → amarillo */
    .blue{color:#4cc9f0}
  </style>
</head>
<body>
  <input id="q" oninput="filt()" placeholder="🔍 buscar..." style="position:fixed;top:8px;right:10px;z-index:2;width:160px;background:#16213e;color:#e0e0e0;border:1px solid #2d4a6e;border-radius:6px;padding:5px 10px;font-family:Consolas;font-size:12px">  <!-- ← NUEVO -->
  <h1>🛰️ SRT Network Monitor</h1>
  <p class="info">Próximo refresh en <b id="cd">10:00</b></p>

  <!-- Tarjetas resumen -->
  <div class="stats">
    <div class="stat"><b class="blue">{{ total }}</b>Total rutas</div>
    <div class="stat"><b class="ok">{{ ok }}</b>Connected</div>
    <div class="stat"><b class="err">{{ ko }}</b>Disconnected</div>
    <div class="stat"><b class="warn">{{ other }}</b>Otros</div>
  </div>

  <!-- Tabla con todas las columnas del CSV -->
  <table>
    <thead><tr>{% for c in cols %}<th>{{ c }}</th>{% endfor %}</tr></thead>
    <tbody>
    {% for row in rows %}
      <tr>
      {% for c in cols %}
        {% set v = row[c] | string %}
        {% if   'disconnected' in (v | lower) %}<td class="err">{{ v }}</td>
        {% elif 'connected'    in (v | lower) %}<td class="ok">{{ v }}</td>
        {% elif 'connecting'   in (v | lower) or 'established' in (v | lower) %}<td class="warn">{{ v }}</td>
        {% else %}<td>{{ v }}</td>
        {% endif %}
      {% endfor %}
      </tr>
    {% endfor %}
    </tbody>
  </table>

  <script>
    // Countdown visual hasta el próximo refresh (no bloquea la recarga)
    let s = 3600;
    setInterval(() => {
      s--;
      document.getElementById('cd').textContent =
        String(~~(s / 60)).padStart(2,'0') + ':' + String(s % 60).padStart(2,'0');
    }, 1000);
    function filt(){const q=document.getElementById('q').value.toLowerCase();  // ← NUEVO: normaliza texto buscado
      document.querySelectorAll('tbody tr').forEach(r=>r.style.display=r.textContent.toLowerCase().includes(q)?'':'none')}  // ← NUEVO: oculta/muestra filas
  </script>
</body></html>"""

@app.route("/")
def index():
    df  = pd.read_csv(CSV).fillna("")                # lee el CSV fresco en cada request
    dst = df["Destination State"].str.lower()
    ok  = int((dst == "connected").sum())
    ko  = int((dst == "disconnected").sum())
    return render_template_string(TMPL,
        cols    = df.columns.tolist(),
        rows    = df.to_dict("records"),
        updated = time.strftime("%d/%m/%Y %H:%M:%S"),
        total   = len(df), ok=ok, ko=ko, other=len(df) - ok - ko)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=52420)  # accesible desde la red local