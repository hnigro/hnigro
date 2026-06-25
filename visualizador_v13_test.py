# srt_monitor.py — Visor SRT con Flask, refresh cada 10 min
from flask import Flask, render_template_string
import pandas as pd, time

app = Flask(__name__)
CSV  = "CSV_FILES\\SRT_consolidados.csv"  # ← ruta al archivo CSV

COLS = [               # ← comentar cualquier línea para ocultar esa columna (header + datos)
    "Description",
    "Asset",
    #"Asset Type",
    "Route Name",
    "Source Name",
    "Source Mode",
    "Source Interface",
    "Source Address",
    "Source Protocol",
    "Source Port",
    "S_SSM",
    "Source State",
    "Source BW",
    "Last Update",
    "Destination Name",
    "Destination Protocol",
    "Destination Port",
    "Destination Mode",
    "Destination Interface",
    "Destination IP",
    "Destination BW",
    "Destination State",
    #"BW In Total",
    #"BW Out Total",
]

TMPL = """<!DOCTYPE html><html lang="es">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="3600">  <!-- recarga la página cada 3600 s = 1 hora -->
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
       position:sticky;top:0;white-space:nowrap;z-index:1;cursor:pointer;user-select:none}
    td{padding:4px 8px;border:1px solid #1e3a5f;white-space:nowrap}
    tr:nth-child(even){background:#0f2540} tr:hover{background:#1e4080}
    .ok{color:#06d6a0;font-weight:bold}   /* connected     → verde  */
    .err{color:#ef476f;font-weight:bold}  /* disconnected  → rojo   */
    .warn{color:#ffd166;font-weight:bold} /* connecting    → amarillo */
    .blue{color:#4cc9f0}
    th.asc::after{content:" ▲";font-size:10px}
    th.desc::after{content:" ▼";font-size:10px}
  </style>
</head>
<body>
  <input id="q" oninput="filt()" placeholder="🔍 buscar..." style="position:fixed;top:8px;right:10px;z-index:2;width:160px;background:#16213e;color:#e0e0e0;border:1px solid #2d4a6e;border-radius:6px;padding:5px 10px;font-family:Consolas;font-size:12px">
  <h1>🛰️ SRT Network Monitor</h1>
  <p class="info">Próximo refresh en <b id="cd">60:00</b></p>

  <!-- Tarjetas resumen -->
  <div class="stats">
    <div class="stat"><b class="blue">{{ total }}</b>Total rutas</div>
    <div class="stat"><b class="ok">{{ ok }}</b>Connected</div>
    <div class="stat"><b class="err">{{ ko }}</b>Disconnected</div>
    <div class="stat"><b class="warn">{{ other }}</b>Otros</div>
  </div>

  <!-- Tabla con todas las columnas del CSV -->
  <table id="srt_table">
    <thead>
      <tr>
        {% for c in cols %}
          <th onclick="sortTable({{ loop.index0 }})">{{ c }}</th>
        {% endfor %}
      </tr>
    </thead>
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

    // Filtro de texto libre
    function filt(){
      const q = document.getElementById('q').value.toLowerCase();
      document.querySelectorAll('tbody tr').forEach(r =>
        r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none'
      );
    }

    // Estado del orden actual
    let sortState = { col: -1, dir: 1 };

    // Intenta interpretar números; si no, devuelve texto normalizado
    function parseVal(txt){
      const t = (txt || '').trim();
      if (t === '') return '';

      const normalized = t.replace(',', '.').replace(/[^\d.\-]/g, '');
      const n = Number(normalized);

      if (!Number.isNaN(n) && normalized !== '' && /[\d]/.test(normalized)) {
        return n;
      }
      return t.toLowerCase();
    }

    // Ordena la tabla por índice de columna
    function sortTable(colIdx){
      const tbody = document.querySelector('#srt_table tbody');
      const rows = Array.from(tbody.querySelectorAll('tr'));

      const sameCol = (sortState.col === colIdx);
      sortState.dir = sameCol ? -sortState.dir : 1;
      sortState.col = colIdx;

      rows.sort((a, b) => {
        const aText = a.cells[colIdx] ? a.cells[colIdx].textContent.trim() : '';
        const bText = b.cells[colIdx] ? b.cells[colIdx].textContent.trim() : '';

        const av = parseVal(aText);
        const bv = parseVal(bText);

        if (typeof av === 'number' && typeof bv === 'number') {
          return (av - bv) * sortState.dir;
        }

        return String(av).localeCompare(String(bv), 'es', {
          numeric: true,
          sensitivity: 'base'
        }) * sortState.dir;
      });

      tbody.append(...rows);

      // Flechas visuales en el header
      document.querySelectorAll('#srt_table th').forEach((th, i) => {
        th.classList.remove('asc', 'desc');
        if (i === colIdx) {
          th.classList.add(sortState.dir === 1 ? 'asc' : 'desc');
        }
      });

      // Mantener filtro aplicado después de ordenar
      filt();
    }
  </script>
</body></html>"""

@app.route("/")
def index():
    df  = pd.read_csv(CSV).fillna("")                # lee el CSV fresco en cada request
    for c in ("Source Port", "Destination Port"):   # floats por NaN → convertir a int
        df[c] = df[c].apply(lambda x: int(x) if x != "" else "")
    dst = df["Destination State"].str.lower()
    ok  = int((dst == "connected").sum())
    ko  = int((dst == "disconnected").sum())
    return render_template_string(TMPL,
        cols    = COLS,
        rows    = df[COLS].to_dict("records"),
        updated = time.strftime("%d/%m/%Y %H:%M:%S"),
        total   = len(df), ok=ok, ko=ko, other=len(df) - ok - ko)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=52420)  # accesible desde la red local