import tkinter as tk

class Window(tk.Tk):

    def __init__(self, width=500, height=500, title="default"):
        super().__init__()
        self.geometry(""+str(width) + "x" + str(height))
        self.title(title)
        self['padx'] = 50


class Table(tk.Frame):
    def __init__(self, parent, rows, columns, header: list, assets: dict):
        tk.Frame.__init__(self, parent)

        self.rows = rows
        self.columns = columns

        # Create labels for column headings
        for idx, h in enumerate(header):
            label = tk.Label(self, text=h)
            label.grid(row=0, column=idx, sticky="nsew")

        # # Place the entry widgets on the grid
        # for row in range(rows):
        #     for col in range(columns):
        #         self.entries[row][col].grid(row=row + 1, column=col, sticky="nsew")

        # Set row and column weights to make the grid scalable
        for i in range(rows + 1):
            self.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)


