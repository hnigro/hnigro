import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ── Configuración ──────────────────────────────────────────────────────────────
CSV   = 'SRT_consolidados.csv'
COLS  = ['Description','Asset','Source Name','Source State','Source BW',
         'Destination Name','Destination State','Destination BW','BW In Total','BW Out Total','Last Update']
WIDTHS= [220,90,130,110,90,130,120,100,90,90,120]
TAGS  = {'ok':'#a6e3a1', 'err':'#f38ba8', 'warn':'#fab387', 'na':'#6c7086'}
BG, BG2, FG = '#1e1e2e', '#313244', '#cdd6f4'
STATE_COLOR = {'connected':'#a6e3a1','disconnected':'#f38ba8',
               'connecting':'#fab387','connection established':'#fab387'}

def load():
    return pd.read_csv(CSV, encoding='latin1').fillna('')

def row_tag(r):
    ss, ds = str(r['Source State']).lower(), str(r['Destination State']).lower()
    return ('ok'  if ss == 'connected'    and ds == 'connected'    else
            'err' if 'disconnected' in (ss, ds)                    else
            'warn' if ss in ('connecting','connection established') else 'na')

# ── Ventana principal ──────────────────────────────────────────────────────────
df = load()
root = tk.Tk()
root.title('🛰  SRT Monitor')
root.geometry('1450x820')
root.configure(bg=BG)

style = ttk.Style()
style.theme_use('clam')
style.configure('Treeview', background=BG2, foreground=FG, fieldbackground=BG2, rowheight=24, font=('Consolas',9))
style.configure('Treeview.Heading', background='#45475a', foreground='#cba6f7', font=('Consolas',9,'bold'))
style.map('Treeview', background=[('selected','#585b70')])

# ── Panel izquierdo ────────────────────────────────────────────────────────────
left = tk.Frame(root, bg='#181825', width=250)
left.pack(side='left', fill='y', padx=(8,4), pady=8)
left.pack_propagate(False)

tk.Label(left, text='🛰 SRT MONITOR',  bg='#181825', fg='#cba6f7', font=('Consolas',11,'bold')).pack(pady=(12,2))
tk.Label(left, text='Seleccioná las rutas a monitorear', bg='#181825', fg='#6c7086', font=('Consolas',8)).pack()

q_var = tk.StringVar()
tk.Entry(left, textvariable=q_var, bg=BG2, fg=FG, insertbackground=FG,
         font=('Consolas',9), relief='flat', bd=6).pack(fill='x', padx=8, pady=6)

# Scroll de checkboxes
cf = tk.Frame(left, bg='#181825')
cf.pack(fill='both', expand=True, padx=4)
cv  = tk.Canvas(cf, bg='#181825', highlightthickness=0)
vsb = tk.Scrollbar(cf, orient='vertical', command=cv.yview)
sf  = tk.Frame(cv, bg='#181825')
sf.bind('<Configure>', lambda e: cv.configure(scrollregion=cv.bbox('all')))
cv.create_window((0, 0), window=sf, anchor='nw')
cv.configure(yscrollcommand=vsb.set)
cv.pack(side='left', fill='both', expand=True)
vsb.pack(side='right', fill='y')
cv.bind_all('<MouseWheel>', lambda e: cv.yview_scroll(int(-1*(e.delta/120)), 'units'))

chk_vars = {n: tk.BooleanVar() for n in sorted(df['Description'].unique())}

def rebuild_checks(*_):
    q = q_var.get().lower()
    for w in sf.winfo_children(): w.destroy()
    for asset in sorted(df['Asset'].unique()):
        names = sorted(df[df['Asset']==asset]['Description'].unique())
        names = [n for n in names if not q or q in n.lower()]
        if not names: continue
        tk.Label(sf, text=f'── {asset} ──', bg='#181825', fg='#585b70',
                 font=('Consolas',8)).pack(anchor='w', padx=4, pady=(6,0))
        for name in names:
            short = name if len(name) <= 30 else '…' + name[-28:]
            tk.Checkbutton(sf, text=short, variable=chk_vars[name],
                           bg='#181825', fg=FG, selectcolor=BG2,
                           activebackground='#181825', activeforeground='#cba6f7',
                           font=('Consolas',8), anchor='w', command=update
                           ).pack(fill='x', padx=6, pady=1)

q_var.trace('w', rebuild_checks)

# Botones Todos / Ninguno
bf = tk.Frame(left, bg='#181825')
bf.pack(fill='x', padx=8, pady=8)
tk.Button(bf, text='☑ Todos', bg=BG2, fg='#a6e3a1', relief='flat',
          font=('Consolas',9), command=lambda: [v.set(True) for v in chk_vars.values()] or update()
          ).pack(side='left', fill='x', expand=True, padx=(0,2))
tk.Button(bf, text='☐ Ninguno', bg=BG2, fg='#f38ba8', relief='flat',
          font=('Consolas',9), command=lambda: [v.set(False) for v in chk_vars.values()] or update()
          ).pack(side='left', fill='x', expand=True)

# Última actualización
last_var = tk.StringVar(value='')
tk.Label(left, textvariable=last_var, bg='#181825', fg='#6c7086', font=('Consolas',7)).pack(pady=4)

# ── Panel derecho ──────────────────────────────────────────────────────────────
right = tk.Frame(root, bg=BG)
right.pack(side='left', fill='both', expand=True, padx=(4,8), pady=8)

# Barra de estadísticas
stats_var = tk.StringVar()
tk.Label(right, textvariable=stats_var, bg=BG, fg='#89b4fa',
         font=('Consolas',10), anchor='w').pack(fill='x', pady=(0,4))

# Gráfico de BW
fig = Figure(figsize=(10, 2.4), facecolor=BG)
ax  = fig.add_subplot(111)
ax.set_facecolor(BG2)
chart = FigureCanvasTkAgg(fig, master=right)
chart.get_tk_widget().pack(fill='x', pady=(0,6))

def draw_chart(fdf):
    ax.clear()
    ax.set_facecolor(BG2)
    fig.patch.set_facecolor(BG)
    if fdf.empty:
        chart.draw(); return
    top = fdf.nlargest(18, 'Source BW') if len(fdf) > 18 else fdf.copy()
    bw  = pd.to_numeric(top['Source BW'], errors='coerce').fillna(0)
    labels  = [n[-26:] for n in top['Description']]
    colors  = [STATE_COLOR.get(str(s).lower(), '#6c7086') for s in top['Source State']]
    ax.barh(labels, bw, color=colors, height=0.6)
    ax.set_xlabel('Source BW (Mbps)', color='#6c7086', fontsize=8)
    ax.tick_params(colors='#6c7086', labelsize=7)
    ax.set_title('Ancho de banda por ruta (top 18)', color='#cba6f7', fontsize=9, pad=4)
    for spine in ax.spines.values(): spine.set_edgecolor('#45475a')
    fig.tight_layout(pad=0.5)
    chart.draw()

# Tabla
tf = tk.Frame(right, bg=BG)
tf.pack(fill='both', expand=True)
tree = ttk.Treeview(tf, columns=COLS, show='headings')
for col, w in zip(COLS, WIDTHS):
    tree.heading(col, text=col)
    tree.column(col, width=w, anchor='w', minwidth=60)
for tag, color in TAGS.items():
    tree.tag_configure(tag, foreground=color)
vsb2 = ttk.Scrollbar(tf, orient='vertical',   command=tree.yview)
hsb2 = ttk.Scrollbar(tf, orient='horizontal', command=tree.xview)
tree.configure(yscrollcommand=vsb2.set, xscrollcommand=hsb2.set)
hsb2.pack(side='bottom', fill='x')
vsb2.pack(side='right',  fill='y')
tree.pack(side='left',   fill='both', expand=True)

# ── Lógica de actualización ────────────────────────────────────────────────────
def update(*_):
    sel  = [k for k, v in chk_vars.items() if v.get()]
    fdf  = df[df['Description'].isin(sel)] if sel else df.copy()
    tree.delete(*tree.get_children())
    for _, r in fdf.iterrows():
        vals = tuple(str(r[c]) if r[c] != '' else '—' for c in COLS)
        tree.insert('', 'end', values=vals, tags=(row_tag(r),))
    ok   = sum(1 for _, r in fdf.iterrows() if row_tag(r) == 'ok')
    err  = sum(1 for _, r in fdf.iterrows() if row_tag(r) == 'err')
    warn = sum(1 for _, r in fdf.iterrows() if row_tag(r) == 'warn')
    stats_var.set(f'  Total: {len(fdf)}   ✅ Conectados: {ok}   '
                  f'❌ Desconectados: {err}   ⚠  Intermedios: {warn}')
    draw_chart(fdf)

def auto_refresh():
    global df
    df = load()
    rebuild_checks()
    update()
    import datetime
    last_var.set('↻ ' + datetime.datetime.now().strftime('%H:%M:%S'))
    root.after(30_000, auto_refresh)   # refresca cada 30 segundos

# ── Arranque ───────────────────────────────────────────────────────────────────
rebuild_checks()
update()
root.after(30_000, auto_refresh)
root.mainloop()
