import tkinter as tk
from app.main_frame import MainFrame
from infrastructure.config_loader import ConfigLoader


class App(tk.Tk):
    """
    Główna klasa aplikacji
    """
    def __init__(self):
        super().__init__()
        self.title("Projekt 2")
        self.geometry('300x500')
        self.lines_map = ConfigLoader.load_config()
        MainFrame(self)
        self.mainloop()
