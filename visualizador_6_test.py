"""
pasado a produccion 08/06/26
v6: auto-refresh del CSV cada 10 minutos  # ← NUEVO
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd

CSV      = "CSV_FILES\\SRT_consolidados.csv"
ALL_COLS = ['Description','Asset','Asset Type','Route Name','Source Name','Source Mode',
            'Source Interface','Source Address','Source Protocol','Source Port','S_SSM',
            'Source State','Source BW','Last Update','Destination Name','Destination Protocol',
            'Destination Port','Destination Mode','Destination Interface','Destination IP',
            'Destination BW','Destination State','BW In Total','BW Out Total']
DEFAULT  = {'Description','Asset','Source State','Source BW','Destination State','Destination BW','Last Update'}
CLR      = {'connected':'#a6e3a1','disconnected':'#f38ba8','connecting':'#fab387','connection established':'#fab387'}
df       = pd.read_csv(CSV, encoding='latin1').fillna('—')
df_str   = df[ALL_COLS].astype(str).apply(lambda r: ' '.join(r).lower(), axis=1)
cur      = [None]

# definida aquí: Python resuelve col_v/cnt al momento del CLICK, no al definir la función
def save():
    cols = [c for c in ALL_COLS if col_v[c].get()] or ALL_COLS
    cur[0][cols].to_csv("CSV_FILES\\resultado_visualizador.csv", index=False)
    cnt.set(cnt.get() + '\n guardado')

root = tk.Tk(); root.title('SRT Monitor'); root.geometry('1300x720'); root.configure(bg='#1e1e2e')
s = ttk.Style(); s.theme_use('clam')
s.configure('Treeview', background='#313244', foreground='#cdd6f4', fieldbackground='#313244', rowheight=22, font=('Consolas',9))
s.configure('Treeview.Heading', background='#45475a', foreground='#cba6f7', font=('Consolas',9,'bold'))

# ── Panel izquierdo ────────────────────────────────────────────────────────────
lf = tk.Frame(root, bg='#181825', width=185); lf.pack(side='left', fill='y', padx=8, pady=8); lf.pack_propagate(False)

# 🔍 Buscador
tk.Label(lf, text='🔍 SEARCH', bg='#181825', fg='#cba6f7', font=('Consolas',10,'bold')).pack(pady=(10,4))
q_var = tk.StringVar()
q_var.trace('w', lambda *_: update())
tk.Entry(lf, textvariable=q_var, bg='#313244', fg='#cdd6f4', insertbackground='#cdd6f4',
         relief='flat', font=('Consolas',9), bd=6).pack(fill='x', padx=8)
tk.Button(lf, text='✕ CLEAN', bg='#313244', fg='#f38ba8', relief='flat',
          font=('Consolas',8), command=lambda: q_var.set('')).pack(pady=(2,4))

tk.Frame(lf, bg='#45475a', height=1).pack(fill='x', padx=8, pady=4)

# 🛰 Assets
tk.Label(lf, text='SERVIDORES', bg='#181825', fg='#cba6f7', font=('Consolas',10,'bold')).pack(pady=(4,4))
asset_v = {a: tk.BooleanVar(value=True) for a in sorted(df['Asset'].unique())}
[tk.Checkbutton(lf, text=a, variable=v, command=lambda: update(),
    bg='#181825', fg='#cdd6f4', selectcolor='#313244', activebackground='#181825',
    font=('Consolas',9)).pack(anchor='w', padx=10, pady=1) for a, v in asset_v.items()]

tk.Frame(lf, bg='#45475a', height=1).pack(fill='x', padx=8, pady=4)

# 💾 Botón save — antes del expand=True de columnas para que siempre sea visible
tk.Button(lf, text='SAVE', bg='#45475a', fg='#a6e3a1', relief='flat',
          font=('Consolas',9,'bold'), command=save).pack(pady=4, padx=8, fill='x')

tk.Frame(lf, bg='#45475a', height=1).pack(fill='x', padx=8, pady=4)

# 📋 Columnas con scroll
tk.Label(lf, text='📋 COLUMNAS', bg='#181825', fg='#cba6f7', font=('Consolas',10,'bold')).pack(pady=(0,4))
wrap = tk.Frame(lf, bg='#181825'); wrap.pack(fill='both', expand=True)
cv   = tk.Canvas(wrap, bg='#181825', highlightthickness=0)
sb   = tk.Scrollbar(wrap, orient='vertical', command=cv.yview)
sf   = tk.Frame(cv, bg='#181825')
sf.bind('<Configure>', lambda e: cv.configure(scrollregion=cv.bbox('all')))
cv.create_window((0,0), window=sf, anchor='nw'); cv.configure(yscrollcommand=sb.set)
sb.pack(side='right', fill='y'); cv.pack(side='left', fill='both', expand=True)
cv.bind_all('<MouseWheel>', lambda e: cv.yview_scroll(int(-1*(e.delta/120)), 'units'))

col_v = {c: tk.BooleanVar(value=c in DEFAULT) for c in ALL_COLS}
[tk.Checkbutton(sf, text=c, variable=v, command=lambda: update(),
    bg='#181825', fg='#cdd6f4', selectcolor='#313244', activebackground='#181825',
    font=('Consolas',8)).pack(anchor='w', padx=6, pady=1) for c, v in col_v.items()]

cnt = tk.StringVar()
tk.Label(lf, textvariable=cnt, bg='#181825', fg='#6c7086', font=('Consolas',8), justify='left').pack(pady=6, padx=8)

# ── Panel derecho: tabla ───────────────────────────────────────────────────────
rf = tk.Frame(root, bg='#1e1e2e'); rf.pack(side='left', fill='both', expand=True, padx=(0,8), pady=8)
tree = ttk.Treeview(rf, columns=ALL_COLS, show='headings')
[tree.heading(c, text=c) or tree.column(c, width=130, minwidth=50) for c in ALL_COLS]
[tree.tag_configure(k, foreground=v) for k, v in CLR.items()]
vsb2 = ttk.Scrollbar(rf, orient='vertical',   command=tree.yview)
hsb2 = ttk.Scrollbar(rf, orient='horizontal', command=tree.xview)
tree.configure(yscrollcommand=vsb2.set, xscrollcommand=hsb2.set)
hsb2.pack(side='bottom', fill='x'); vsb2.pack(side='right', fill='y'); tree.pack(fill='both', expand=True)

# ── Lógica ─────────────────────────────────────────────────────────────────────
def update():
    sel = [a for a, v in asset_v.items() if v.get()]
    mask = df['Asset'].isin(sel)
    q = q_var.get().strip().lower()
    if q: mask &= df_str.str.contains(q, na=False)
    fdf = df[mask]
    cur[0] = fdf
    tree['displaycolumns'] = [c for c in ALL_COLS if col_v[c].get()] or ALL_COLS
    tree.delete(*tree.get_children())
    [tree.insert('', 'end', values=[r[c] for c in ALL_COLS],
        tags=(str(r['Source State']).lower(),)) for _, r in fdf.iterrows()]
    ok = (fdf['Source State'].str.lower() == 'connected').sum()
    cnt.set(f'Rutas: {len(fdf)}\n✅ {ok}\n❌ {len(fdf)-ok}')

# ── Auto-refresh ───────────────────────────────────────────────────────────────
def auto_refresh():                                                              # ← NUEVO
    global df, df_str                                                            # ← NUEVO
    df     = pd.read_csv(CSV, encoding='latin1').fillna('—')                    # ← NUEVO
    df_str = df[ALL_COLS].astype(str).apply(lambda r: ' '.join(r).lower(), axis=1)  # ← NUEVO
    update()                                                                     # ← NUEVO
    root.after(1000, auto_refresh)                                           # ← NUEVO (loop)

update()
root.after(1000, auto_refresh)                                               # ← NUEVO (primer ciclo)
root.mainloop()