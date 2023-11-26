import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        tk.Label(self, text="From:").grid(row=0, column=0)
        self.from_entry = tk.Entry(self)
        self.from_entry.grid(row=0, column=1)

        tk.Label(self, text="To:").grid(row=1, column=0)
        self.to_entry = tk.Entry(self)
        self.to_entry.grid(row=1, column=1)

        self.pack()
