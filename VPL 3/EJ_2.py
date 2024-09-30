class Oxzutify:
    def __init__(self):
        self.library = {
            "Kanye West": {
                "albums": {
                    "The College Dropout": ["All Falls Down", "Jesus Walks", "Through the Wire"],
                    "Graduation": ["Stronger", "Good Life", "Flashing Lights"]
                }
            },
            "Kendrick Lamar": {
                "albums": {
                    "good kid, m.A.A.d city": ["Swimming Pools", "Bitch, Don't Kill My Vibe", "Money Trees"],
                    "DAMN.": ["HUMBLE.", "DNA.", "LOVE."]
                }
            },
            "MF DOOM": {
                "albums": {
                    "MM..FOOD": ["Beef Rapp", "Hoe Cakes", "Potholderz"],
                    "Madvillainy": ["Accordion", "Meat Grinder", "Figaro"]
                }
            },
            "Travis Scott": {
                "albums": {
                    "Rodeo": ["Antidote", "3500", "90210"],
                    "Astroworld": ["SICKO MODE", "STARGAZING", "STOP TRYING TO BE GOD"]
                }
            },
            "XXXTentacion": {
                "albums": {
                    "17": ["Jocelyn Flores", "Everybody Dies in Their Nightmares", "Revenge"],
                    "?": ["SAD!", "changes", "Moonlight"]
                }
            }
        }

    def select_from_list(self, items, prompt):
        while True:
            print(f"\n--- {prompt} ---")
            for i, item in enumerate(items):
                print(f"{i + 1}. {item}")
            print("0. Volver")
            choice = input("Elige una opción: ")
            if choice == '':
                print("Entrada vacía. Por favor, intenta de nuevo.")
                continue
            try:
                choice = int(choice) - 1
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
                continue
            if choice == -1:
                return None
            elif 0 <= choice < len(items):
                return items[choice]
            else:
                print("Opción no encontrada.")

    def play_by_artist(self):
        while True:
            artist = self.select_from_list(list(self.library.keys()), "Lista de Artistas")
            if artist is None:
                break
            print(f"\n--- Reproduciendo canciones de {artist} ---")
            for album, songs in self.library[artist]["albums"].items():
                for song in songs:
                    print(f"- {song}")

    def play_by_album(self):
        while True:
            artist = self.select_from_list(list(self.library.keys()), "Lista de Artistas")
            if artist is None:
                break
            while True:
                album = self.select_from_list(list(self.library[artist]["albums"].keys()), f"Álbumes de {artist}")
                if album is None:
                    break
                print(f"\n--- Reproduciendo canciones del álbum {album} de {artist} ---")
                for song in self.library[artist]["albums"][album]:
                    print(f"- {song}")

    def play_by_song(self):
        while True:
            artist = self.select_from_list(list(self.library.keys()), "Lista de Artistas")
            if artist is None:
                break
            while True:
                album = self.select_from_list(list(self.library[artist]["albums"].keys()), f"Álbumes de {artist}")
                if album is None:
                    break
                while True:
                    song = self.select_from_list(self.library[artist]["albums"][album], f"Canciones del álbum {album} de {artist}")
                    if song is None:
                        break
                    print(f"\n--- Reproduciendo {song} de {artist} del álbum {album} ---")

    def main(self):
        while True:
            print("---------------------------")
            print("\nOxzutify")
            print("1. Reproducir por Artista")
            print("2. Reproducir por Álbum")
            print("3. Reproducir por Canción")
            print("4. Salir")
            choice = input("Elige una opción: ")

            if choice == '':
                print("Entrada vacía. Por favor, intenta de nuevo.")
                continue
            if choice == "1":
                self.play_by_artist()
            elif choice == "2":
                self.play_by_album()
            elif choice == "3":
                self.play_by_song()
            elif choice == "4":
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    service = Oxzutify()
    service.main()