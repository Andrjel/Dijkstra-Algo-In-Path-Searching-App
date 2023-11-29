import tkinter as tk
from tkinter import messagebox
from infrastructure.dij_alg import Dijkstra


class MainFrame(tk.Frame):
    """
    Główna ramka aplikacji
    """
    def __init__(self, parent):
        super().__init__(parent)
        options = {'padx': 10, 'pady': 10}
        # Okno aplikacji
        self.parent = parent

        # Pole wyszukiwania
        tk.Label(self, text="From:").grid(row=0, column=0, **options)
        self.search_from = tk.StringVar(value="Turkusowa")
        self.from_entry = tk.Entry(self, width=30, textvariable=self.search_from)
        self.from_entry.grid(row=0, column=1, **options)

        tk.Label(self, text="To:").grid(row=1, column=0, **options)
        self.search_to = tk.StringVar(value="Podbórz")
        self.to_entry = tk.Entry(self, width=30, textvariable=self.search_to)
        self.to_entry.grid(row=1, column=1, **options)

        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.grid(row=2, column=0, columnspan=2, **options)

        self.pack()

    def search(self):
        """Wyszukiwanie połączenia"""

        # Sprawdzenie, czy pola z nawazmi przystanków nie są puste
        if self.search_from.get() == '' or self.search_to.get() == '':
            return
        try:
            # Wywołanie algorytmu Dijkstry - Wyszukanie połączenia
            result = Dijkstra(self.parent.lines_map).get_route(self.search_from.get(), self.search_to.get())
        except Exception:
            # W przypadku błędu wyświetlenie komunikatu
            messagebox.showerror("Error", "Path not reachable")
            return

        # Czyszczenie poprzednich wyników
        if hasattr(self, 'result_frame'):
            self.result_frame.destroy()
        self.result_frame = tk.Frame(self)
        self.result_frame.grid(row=3, column=0, columnspan=2, **{'padx': 10, 'pady': 10})

        # Wyszukanie wszystkich linii wykorzystanych w przejeździe
        lines = []
        for idx, name in enumerate(result):
            if idx < len(result) - 1 and name[2] not in lines:
                lines.append(name[2])

        # wyświetlenie wyników
        for line in lines:
            suma = 0
            for idx, name in enumerate(result):
                if idx < len(result) - 1 and name[2] == line:
                    suma += name[1]
            disp_text = line + " (" + str(suma) + " min):"
            tk.Label(self.result_frame, text=disp_text, font=("Arial", 15), fg="blue").pack()
            for idx, name in enumerate(result):
                if idx < len(result) - 1 and name[2] == line:
                    tk.Label(self.result_frame, text=f"{name[0]} ->").pack()
        tk.Label(self.result_frame, text=result[-1][0], fg="red").pack()
