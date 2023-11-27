import tkinter as tk


class MainFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        options = {'padx': 10, 'pady': 10}
        self.parent = parent

        tk.Label(self, text="From:").grid(row=0, column=0, **options)
        self.from_entry = tk.Entry(self, width=30)
        self.from_entry.grid(row=0, column=1, **options)

        tk.Label(self, text="To:").grid(row=1, column=0, **options)
        self.to_entry = tk.Entry(self, width=30)
        self.to_entry.grid(row=1, column=1, **options)

        self.search_button = tk.Button(self, text="Search")
        self.search_button.grid(row=2, column=0, columnspan=2, **options)

        self.pack()
