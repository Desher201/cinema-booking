import json
from pathlib import Path


class Movie:
    json_path = Path("films.json")
    id = 0

    def __init__(self, title, director, genre):
        self.title = title
        self.director = director
        self.genre = genre
        self.id = Movie.id
        Movie.id += 1

    def add_film_to_json(self):
        if not self.json_path.exists():
            with open(self.json_path, "w", encoding="utf8") as json_file:
                json.dump([], json_file)

        with open(self.json_path, "r+", encoding="utf8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []
            if not any(i["id"] == self.id for i in data) and not any(i["title"] == self.title for i in data):
                data.append(self.__dict__)



            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

    @staticmethod
    def show_all_films():
        with open("films.json", "r", encoding="utf8") as f:
            try:
                data = json.load(f)
                print("=" * 100)
                for i in data:
                    print(f"id:{i["id"]}, title:{i["title"]}, director:{i['director']}, genre:{i['genre']}")
                print("=" * 100)
            except json.decoder.JSONDecodeError:
                print("error")

    @staticmethod
    def find_film_by_id(id):
        with open("films.json", "r", encoding="utf8") as f:
            data = json.load(f)
            for i in data:
                if i["id"] == id:
                    print(f"id:{i["id"]}, title:{i["title"]}, director:{i['director']}, genre:{i['genre']}")


movie = Movie("Interstellar", "Christopher Nolan", "")
movie_2 = Movie("neInterstellar", "neChristopher Nolan", "")
movie_3 = Movie("Interstellar", "neChristopher Nolan", "")
movie.add_film_to_json()
movie_2.add_film_to_json()
movie.show_all_films()
Movie.find_film_by_id(movie.id)
