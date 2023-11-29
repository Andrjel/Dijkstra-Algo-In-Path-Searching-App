import json
import os


class Config:
    """Klasa do tworzenia plików konfiguracyjnych (json) dla linii autobusowych."""
    def __init__(self):
        self.__data: dict = {}

    def save_file(self, file_name: str) -> None:
        """Zapisuje plik konfiguracyjny."""
        with open(file_name, "w") as file:
            json.dump(self.__data, file, indent=4)

    def insert_data(self) -> None:
        """Pozwala na wprowadzenie danych do pliku konfiguracyjnego."""
        while True:
            os.system("cls")
            bus_stop_name = input("Podaj nazwę przystanku: ")
            neighbour_bus_stop = input("Podaj przystanek sąsiedni: ")
            weight = input("Podaj odległośc do przystanku sąsiedniego: ")
            self.__data.update({bus_stop_name: {neighbour_bus_stop: weight}})
            print("Czy chcesz dodać kolejny przystanek?(t/n)")
            if input() == "n":
                break
        line_number = input("Podaj numer linii: ")
        self.save_file(f"linia_{line_number}.json")


def main():
    config = Config()
    config.insert_data()


if __name__ == "__main__":
    main()
