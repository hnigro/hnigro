"""
visualizador_v8.py
v7: manejo de excepciones si el CSV no se encuentra
v8: Flask web server — misma UI accesible por IP:Puerto   # ← NUEVO
"""
from flask import Flask, jsonify
import pandas as pd

CSV      = "CSV_FILE\\SRT_consolidados.csv"
ALL_COLS = ['Description','Asset','Asset Type','Route Name','Source Name','Source Mode',
            'Source Interface','Source Address','Source Protocol','Source Port','S_SSM',
            'Source State','Source BW','Last Update','Destination Name','Destination Protocol',
            'Destination Port','Destination Mode','Destination Interface','Destination IP',
            'Destination BW','Destination State','BW In Total','BW Out Total']

app = Flask(__name__)

def load():                                                        # igual que v7
    try:    return pd.read_csv(CSV, encoding='latin1').fillna('—')
    except: return pd.DataFrame(columns=ALL_COLS)

@app.route('/data')                                                # ← NUEVO: entrega JSON al browser
def data():
    df = load()
    return jsonify({'cols'  : ALL_COLS,
                    'rows'  : df[ALL_COLS].values.tolist(),
                    'assets': sorted(df['Asset'].dropna().unique().tolist())})

@app.route('/')                                                    # ← NUEVO: página principal
def index(): return HTML   # Flask devuelve text/html SIN pasar por Jinja2

HTML = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8"><title>SRT Monitor</title>
<style>
*{box-sizing:border-box;margin:0;padding:0;font-family:Consolas,monospace}
body{background:#1e1e2e;color:#cdd6f4;display:flex;height:100vh;overflow:hidden}
#lf{width:185px;background:#181825;padding:8px;display:flex;flex-direction:column;overflow:hidden}
.lbl{color:#cba6f7;font-weight:bold;font-size:10px;padding:6px 0 2px}
input[type=text]{width:100%;background:#313244;color:#cdd6f4;border:none;padding:5px 6px;font:9px Consolas;outline:none}
button{background:#45475a;color:#a6e3a1;border:none;padding:4px;cursor:pointer;font:bold 9px Consolas;width:100%}
.bx{background:#313244;color:#f38ba8;margin:2px 0}
hr{border:none;border-top:1px solid #45475a;margin:4px 0}
.scr{overflow-y:auto;flex:1}
label{display:block;padding:1px 4px;cursor:pointer;white-space:nowrap;font-size:8px}
#cnt{color:#6c7086;font-size:8px;padding:4px;white-space:pre}
#rf{flex:1;overflow:auto;padding:8px}
table{border-collapse:collapse;font-size:9px;white-space:nowrap}
th{background:#45475a;color:#cba6f7;font-weight:bold;padding:4px 8px;position:sticky;top:0;z-index:1}
td{background:#313244;padding:3px 8px;border-bottom:1px solid #1e1e2e}
tr[data-s=connected] td{color:#a6e3a1}
tr[data-s=disconnected] td{color:#f38ba8}
tr[data-s=connecting] td,tr[data-s="connection established"] td{color:#fab387}
</style></head>
<body>
<div id="lf">
  <div class="lbl">🔍 SEARCH</div>
  <input type="text" id="q" oninput="render()">
  <button class="bx" onclick="document.getElementById('q').value='';render()">✕ CLEAN</button>
  <hr>
  <div class="lbl">🛰 SERVIDORES</div>
  <div id="ap"></div>
  <hr>
  <button onclick="save()">💾 SAVE</button>
  <hr>
  <div class="lbl">📋 COLUMNAS</div>
  <div class="scr" id="cp"></div>
  <div id="cnt"></div>
</div>
<div id="rf">
  <table><thead id="th"></thead><tbody id="tb"></tbody></table>
</div>
<script>
let rows=[],cols=[],aV={},cV={},flt=[];
const DEF=new Set(['Description','Asset','Source State','Source BW','Destination State','Destination BW','Last Update']);

function mkChk(pid,lbl,chk,fn){
  const l=document.createElement('label'),i=document.createElement('input');
  Object.assign(i,{type:'checkbox',checked:chk,onchange:fn});
  i.style.accentColor='#cba6f7';
  l.append(i,' '+lbl); document.getElementById(pid).appendChild(l);
}

async function poll(){
  const d=await fetch('/data').then(r=>r.json()).catch(()=>null);
  if(!d){document.getElementById('cnt').textContent='⚠ Sin datos';return;}
  cols=d.cols;
  rows=d.rows.map(r=>Object.fromEntries(cols.map((c,i)=>[c,r[i]])));
  if(!Object.keys(aV).length) d.assets.forEach(a=>{aV[a]=true;mkChk('ap',a,true,e=>{aV[a]=e.target.checked;render();});});
  if(!Object.keys(cV).length) cols.forEach(c=>{cV[c]=DEF.has(c);mkChk('cp',c,DEF.has(c),e=>{cV[c]=e.target.checked;render();});});
  render();
}

function render(){
  const q=document.getElementById('q').value.toLowerCase();
  const vis=cols.filter(c=>cV[c]);
  flt=rows.filter(r=>(aV[r.Asset]??true)&&(!q||Object.values(r).join(' ').toLowerCase().includes(q)));
  document.getElementById('th').innerHTML='<tr>'+vis.map(c=>`<th>${c}</th>`).join('')+'</tr>';
  document.getElementById('tb').innerHTML=flt.map(r=>{
    const s=(r['Source State']||'').toLowerCase();
    return `<tr data-s="${s}">`+vis.map(c=>`<td>${r[c]||''}</td>`).join('')+'</tr>';
  }).join('');
  const ok=flt.filter(r=>(r['Source State']||'').toLowerCase()==='connected').length;
  document.getElementById('cnt').textContent=`Rutas: ${flt.length}\n✅ ${ok}\n❌ ${flt.length-ok}`;
}

function save(){
  const vc=cols.filter(c=>cV[c]),c=vc.length?vc:cols;
  const csv=[c.join(','),...flt.map(r=>c.map(k=>`"${(r[k]||'').replace(/"/g,'""')}"`).join(','))].join('\n');
  Object.assign(document.createElement('a'),
    {href:URL.createObjectURL(new Blob([csv],{type:'text/csv'})),download:'resultado_visualizador.csv'}
  ).click();
}

poll(); setInterval(poll, 3000);  // ← intervalo de refresh en ms (3000 = 3 seg)
</script>
</body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # ← cambiar puerto aquí