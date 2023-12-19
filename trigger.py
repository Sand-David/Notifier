import tkinter as tk
from app import App
from widgets import Table

def init_overview(symbols: list = []):
    menue = App(title="Overview")

    if not symbols:
        info = tk.Label(text="There are no triggered asset values.").pack()
        btn = tk.Button(menue, text="Abort", command=menue.destroy).pack()
        menue.mainloop()
        return

    #define dict using symbols in scraper
    fetched_assets = {'BTC': 1, 'ETH': 2}
    list_stock_info(menue, fetched_assets)

    tk.Button(menue, text='Show Details', command=menue.next_window()).pack()
    tk.Button(menue, text='Abort', command=menue.destroy).pack()
    #tk.Frame(background='lightgreen').pack()
    menue.mainloop()
    return 
        
def list_stock_info(window: App, assets: dict = {}):
    #get info via scraper
    row = len(assets)
    col = 2
    header = ["Symbol", "Current Price"]
    table = Table(window, row, col, header, assets)
    #tk.Frame(background='lightgreen').pack()
    table.pack(expand=True, fill="both")
        
def show_details():
    pass

import tkinter as tk
