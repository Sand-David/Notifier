import tkinter as tk

class App(tk.Tk):

    def __init__(self, width=500, height=500, title="default"):
        super().__init__()
        self.geometry(""+str(width) + "x" + str(height))
        self.title(title)
        self['padx'] = 50

    def next_window(self, title="default"):
        new_window = tk.Toplevel(self)
        new_window.title(title)

        label = tk.Label(new_window, text="this is a new window!")
        label.pack(padx=20, pady=20)

        