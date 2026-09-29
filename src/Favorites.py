import json
from pathlib import Path


class Favorites:
    favorites_path = Path("favorites.json")

    @staticmethod
    def add_to_favorites():
        with open("films.json", "r", encoding="utf8") as f:
            try:
                films = json.load(f)
            except json.decoder.JSONDecodeError:
                films = []

        for film in films:
            print(
                f"id:{film['id']}, "
                f"title:{film['title']}, "
                f"director:{film['director']}, "
                f"genre:{film['genre']}"
            )
        with open(Favorites.favorites_path, "r", encoding="utf8") as f:
            try:
                favorite_films = json.load(f)
            except json.decoder.JSONDecodeError:
                favorite_films = []


        film_id = int(input("Введіть id фільму: "))

        selected_film = None
        film_is_repeat = False
        for i in favorite_films:
            if favorite_films:
                if i["id"] == film_id:
                    print("Такий фільм вже додано до обраних.")
                    film_is_repeat = True
                    break
        if not film_is_repeat:
            for film in films:
                if film["id"] == film_id:
                    selected_film = film
                    break

            if selected_film is None:
                print("Такого фільму немає")
                return

        if not Favorites.favorites_path.exists():
            with open(Favorites.favorites_path, "w", encoding="utf8") as f:
                json.dump([], f)

        with open(Favorites.favorites_path, "r+", encoding="utf8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
            if film_is_repeat is False:
                data.append(selected_film)

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
        if film_is_repeat is False:
            print("Фільм додано до обраного")
Favorites.add_to_favorites()
