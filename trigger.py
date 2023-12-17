import tkinter as tk
from window import Window
from window import Table

def init_overview(symbols: list = []):
    menue = Window(title="Overview")

    if not symbols:
        info = tk.Label(text="There are no triggered asset values.").pack()
        btn = tk.Button(menue, text="Abort", command=menue.destroy).pack()
        menue.mainloop()
        return

    #define dict using symbols in scraper
    fetched_assets = {'BTC': 1, 'ETH': 2}
    list_stock_info(menue, fetched_assets)

    tk.Button(menue, text='Show Details').pack()
    tk.Button(menue, text='Abort', command=menue.destroy).pack()
    #tk.Frame(background='lightgreen').pack()
    menue.mainloop()
    return 
        
def list_stock_info(window: Window, assets: dict = {}):
    #get info via scraper
    row = len(assets)
    col = 2
    header = ["Symbol", ""]
    table = Table(window, row, col, header, assets)
    #tk.Frame(background='lightgreen').pack()
    table.pack(expand=True, fill="both")
        


def show_details():
    pass

import tkinter as tk
