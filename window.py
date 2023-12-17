import tkinter as tk

class Window(tk.Tk):

    def __init__(self, width=500, height=500, title="default"):
        super().__init__()
        self.geometry(""+str(width) + "x" + str(height))
        self.title(title)
        self['padx'] = 50