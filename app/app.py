import tkinter as tk
from app.main_frame import MainFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Projekt 2")
        self.geometry('300x500')
        MainFrame(self)
        self.mainloop()
