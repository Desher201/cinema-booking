import json
from pathlib import Path


class Movie:
    json_path = Path("films.json")
    id = 0

    def __init__(self, title, director, genre):
        self.title = title
        self.director = director
        self.genre = genre

        Movie.id += 1
        self.id = Movie.id

    def add_film_to_json(self):

        if not self.json_path.exists():
            with open(self.json_path, "w", encoding="utf8") as json_file:
                json.dump([], json_file)

        with open(self.json_path, "r+", encoding="utf8") as f:
            data = json.load(f)

            data.append(self.__dict__)

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()


movie = Movie("Interstellar", "Christopher Nolan", "Sci-Fi")
movie.add_film_to_json()
