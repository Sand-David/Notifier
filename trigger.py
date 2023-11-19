import tkinter as tk
from window import Window

def fetch_triggered_assets(assets: dict = {}):
    #menue = tk.Tk()
    menue = Window(10, 20)

    if not assets:
        info = tk.Label(text="There are no triggered asset values.").pack()
        btn = tk.Button(menue, text="Abort", command=menue.destroy).pack()
        menue.mainloop()
        return

    for key in assets:
        tk.Checkbutton(menue, name=key.lower(), text=key).pack()
        print(assets[key])
    
    tk.Button(menue, text='Show Details').pack()
    tk.Button(menue, text='Abort', command=menue.destroy).pack()
    menue.mainloop()
    return 
        

def show_details():
    pass