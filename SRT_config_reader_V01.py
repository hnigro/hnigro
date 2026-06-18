# Visualizador de canales SRT - Flask en un solo archivo
from flask import Flask, render_template_string
from collections import Counter
import ast

ARCHIVO = "CSV_FILES\\SRT-ABC-01_CONFIG.txt"  # archivo a leer (misma carpeta que este script)

app = Flask(__name__)


def cargar():
    with open(ARCHIVO, encoding="latin-1") as f:
        return ast.literal_eval(f.read())


def aplanar(canales):
    """Genera 1 fila por cada combinación canal+destino (o 1 fila si no hay destinos)."""
    filas = []
    for c in canales:
        s = c["source"]
        for d in c["destinations"] or [{}]:
            filas.append({
                "canal": c["name"], "estado": c["summaryStatusCode"], "detalle": c["summaryStatusDetails"],
                "o_nombre": s.get("name", ""), "o_proto": s.get("protocol", ""),
                "o_dir": s.get("address", ""), "o_puerto": s.get("port", ""),
                "o_bw": s.get("usedBandwidth", ""), "o_lat": s.get("srtLatency", ""),
                "o_estado": s.get("summaryStatusCode", ""), "o_detalle": s.get("summaryStatusDetails", ""),
                "d_nombre": d.get("name", ""), "d_proto": d.get("protocol", ""),
                "d_dir": d.get("address", ""), "d_puerto": d.get("port", ""),
                "d_bw": d.get("usedBandwidth", ""), "d_lat": d.get("srtLatency", ""),
                "d_estado": d.get("summaryStatusCode", ""), "d_detalle": d.get("summaryStatusDetails", ""),
                "d_iniciado": d.get("started"),
            })
    return filas


PLANTILLA = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>SRT-ABC-01 · Monitor de canales</title>
<style>
:root{--bg:#f7f7f5;--card:#fff;--text:#1f2421;--muted:#6b7280;--border:#e3e1da;
--ok:#0f6e56;--ok-bg:#e1f5ee;--warn:#854f0b;--warn-bg:#faeeda;
--error:#a32d2d;--error-bg:#fcebeb;--unknown:#5f5e5a;--unknown-bg:#f1efe8;
--mono:ui-monospace,Consolas,monospace;--sans:-apple-system,"Segoe UI",Roboto,sans-serif}
*{box-sizing:border-box}
body{margin:0;font-family:var(--sans);background:var(--bg);color:var(--text);font-size:14px}
header{padding:16px 20px;background:var(--card);border-bottom:1px solid var(--border)}
h1{margin:0 0 10px;font-size:18px;font-weight:600}
.resumen,.controles{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.controles{margin-top:10px}
.badge{display:inline-block;padding:2px 9px;border-radius:999px;font-size:12px;font-weight:600;background:var(--unknown-bg);color:var(--unknown)}
.badge.ok{background:var(--ok-bg);color:var(--ok)}
.badge.warn{background:var(--warn-bg);color:var(--warn)}
.badge.error{background:var(--error-bg);color:var(--error)}
.total{color:var(--muted);font-size:13px}
input,select{padding:6px 10px;border:1px solid var(--border);border-radius:6px;font-size:13px;background:var(--card);color:var(--text)}
input{flex:0 1 320px;min-width:180px}
table{border-collapse:collapse;width:100%;font-size:12.5px;background:var(--card)}
th,td{padding:6px 9px;border-bottom:1px solid var(--border);white-space:nowrap;text-align:left}
thead th{background:#f0efe9;font-weight:600;border-bottom:2px solid var(--border)}
thead tr:first-child th{text-align:center;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
tbody tr:nth-child(even){background:#fafaf9}
tbody tr:hover{background:#f0efe9}
.mono{font-family:var(--mono);text-align:right}
.proto{text-transform:uppercase;color:var(--muted);font-size:11px}
.sin-destino{color:var(--muted);font-style:italic;text-align:center}
</style>
</head>
<body>
<header>
  <h1>SRT-ABC-01 · Monitor de canales</h1>
  <div class="resumen">
    <span class="badge ok">OK {{ resumen.get('ok',0) }}</span>
    <span class="badge warn">WARN {{ resumen.get('warn',0) }}</span>
    <span class="badge error">ERROR {{ resumen.get('error',0) }}</span>
    <span class="badge">UNKNOWN {{ resumen.get('unknown',0) }}</span>
    <span class="total">{{ total }} canales · {{ filas|length }} filas</span>
  </div>
  <div class="controles">
    <input id="buscar" type="search" placeholder="Buscar canal..." oninput="filtrar()">
    <select id="filtroEstado" onchange="filtrar()">
      <option value="">Todos los estados</option>
      <option value="ok">OK</option>
      <option value="warn">WARN</option>
      <option value="error">ERROR</option>
      <option value="unknown">UNKNOWN</option>
    </select>
  </div>
</header>
<table>
<thead>
<tr><th></th><th></th><th colspan="7">Origen</th><th colspan="8">Destino</th></tr>
<tr>
  <th>Canal</th><th>Estado</th>
  <th>Nombre</th><th>Proto</th><th>Dirección</th><th>Puerto</th><th>Mbps</th><th>Lat ms</th><th>Estado</th>
  <th>Nombre</th><th>Proto</th><th>Dirección</th><th>Puerto</th><th>Mbps</th><th>Lat ms</th><th>Estado</th><th>Iniciado</th>
</tr>
</thead>
<tbody>
{% set etq = {'ok':'OK','warn':'WARN','error':'ERR','unknown':'UNK'} %}
{% for f in filas %}
<tr data-canal="{{ f.canal|lower }}" data-estado="{{ f.estado }}">
  <td>{{ f.canal }}</td>
  <td><span class="badge {{ f.estado }}" title="{{ f.detalle }}">{{ etq.get(f.estado, f.estado) }}</span></td>
  <td>{{ f.o_nombre }}</td>
  <td class="proto">{{ f.o_proto }}</td>
  <td class="mono">{{ f.o_dir }}</td>
  <td class="mono">{{ f.o_puerto }}</td>
  <td class="mono">{{ f.o_bw }}</td>
  <td class="mono">{{ f.o_lat or '-' }}</td>
  <td><span class="badge {{ f.o_estado }}" title="{{ f.o_detalle }}">{{ etq.get(f.o_estado, f.o_estado) }}</span></td>
  {% if f.d_nombre %}
  <td>{{ f.d_nombre }}</td>
  <td class="proto">{{ f.d_proto }}</td>
  <td class="mono">{{ f.d_dir }}</td>
  <td class="mono">{{ f.d_puerto }}</td>
  <td class="mono">{{ f.d_bw }}</td>
  <td class="mono">{{ f.d_lat or '-' }}</td>
  <td><span class="badge {{ f.d_estado }}" title="{{ f.d_detalle }}">{{ etq.get(f.d_estado, f.d_estado) }}</span></td>
  <td>{{ 'Sí' if f.d_iniciado else 'No' }}</td>
  {% else %}
  <td colspan="8" class="sin-destino">— sin destino configurado —</td>
  {% endif %}
</tr>
{% endfor %}
</tbody>
</table>
<script>
function filtrar(){
  const q = document.getElementById('buscar').value.toLowerCase();
  const est = document.getElementById('filtroEstado').value;
  document.querySelectorAll('tbody tr').forEach(tr=>{
    const ok = tr.dataset.canal.includes(q) && (!est || tr.dataset.estado===est);
    tr.style.display = ok ? '' : 'none';
  });
}
</script>
</body>
</html>"""


@app.route("/")
def index():
    canales = cargar()
    return render_template_string(
        PLANTILLA,
        filas=aplanar(canales),
        resumen=Counter(c["summaryStatusCode"] for c in canales),
        total=len(canales),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)