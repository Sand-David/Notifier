import tkinter as tk

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
        #for row in range(1, rows+1):
        for idx, (key, value) in enumerate(assets.items()):
                #self.entries[row][0].grid(row=row + 1, column=0, sticky="nsew")
                symbol = tk.Label(self, text=key)
                symbol.grid(row=idx+1, column=0, sticky="nsew")
                price = tk.Label(self, text=value)
                price.grid(row=idx+1, column=1, sticky="nsew")


        # Set row and column weights to make the grid scalable
        for i in range(rows + 1):
            self.grid_rowconfigure(i) #, weight=1
        for j in range(columns):
            self.grid_columnconfigure(j)


