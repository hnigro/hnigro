import tkinter as tk
from tkinter import ttk
import pandas as pd

CSV  = 'SRT_consolidados.csv'
COLS = ['Description','Asset','Source State','Source BW','Destination State','Destination BW','Last Update']
CLR  = {'connected':'#a6e3a1','disconnected':'#f38ba8','connecting':'#fab387','connection established':'#fab387'}
df   = pd.read_csv(CSV, encoding='latin1').fillna('—')

root = tk.Tk(); root.title('SRT Monitor'); root.geometry('1200x680'); root.configure(bg='#1e1e2e')

# ── Estilos ────────────────────────────────────────────────────────────────────
s = ttk.Style(); s.theme_use('clam')
s.configure('Treeview', background='#313244', foreground='#cdd6f4', fieldbackground='#313244', rowheight=22, font=('Consolas',9))
s.configure('Treeview.Heading', background='#45475a', foreground='#cba6f7', font=('Consolas',9,'bold'))

# ── Panel izquierdo: checkboxes por Asset ──────────────────────────────────────
lf = tk.Frame(root, bg='#181825', width=170); lf.pack(side='left', fill='y', padx=8, pady=8); lf.pack_propagate(False)
tk.Label(lf, text='🛰 ASSETS', bg='#181825', fg='#cba6f7', font=('Consolas',10,'bold')).pack(pady=10)
chk = {a: tk.BooleanVar(value=True) for a in sorted(df['Asset'].unique())}
[tk.Checkbutton(lf, text=a, variable=chk[a], command=lambda: update(),
    bg='#181825', fg='#cdd6f4', selectcolor='#313244', activebackground='#181825',
    font=('Consolas',9)).pack(anchor='w', padx=10, pady=3) for a in chk]

# Contador
cnt = tk.StringVar()
tk.Label(lf, textvariable=cnt, bg='#181825', fg='#6c7086', font=('Consolas',8), justify='left').pack(pady=12, padx=8)

# ── Panel derecho: tabla ───────────────────────────────────────────────────────
rf = tk.Frame(root, bg='#1e1e2e'); rf.pack(side='left', fill='both', expand=True, padx=(0,8), pady=8)
tree = ttk.Treeview(rf, columns=COLS, show='headings')
[tree.heading(c, text=c) or tree.column(c, width=w) for c, w in zip(COLS, [240,90,120,80,130,90,120])]
[tree.tag_configure(k, foreground=v) for k, v in CLR.items()]
vsb = ttk.Scrollbar(rf, orient='vertical', command=tree.yview); vsb.pack(side='right', fill='y')
tree.configure(yscrollcommand=vsb.set); tree.pack(fill='both', expand=True)

# ── Actualizar tabla ───────────────────────────────────────────────────────────
def update():
    sel = [a for a, v in chk.items() if v.get()]
    fdf = df[df['Asset'].isin(sel)]
    tree.delete(*tree.get_children())
    [tree.insert('', 'end', values=[r[c] for c in COLS],
        tags=(str(r['Source State']).lower(),)) for _, r in fdf.iterrows()]
    ok = sum(1 for _, r in fdf.iterrows() if str(r['Source State']).lower() == 'connected')
    cnt.set(f'Rutas: {len(fdf)}\n✅ {ok}\n❌ {len(fdf)-ok}')

update()
root.mainloop()