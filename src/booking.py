import json
from pathlib import Path


class Booking:
    booking_path = Path("bookings.json")
    films_path = Path("films.json")

    @staticmethod
    def book_ticket():
        with open(Booking.films_path, "r", encoding="utf8") as f:
            try:
                films = json.load(f)
            except json.decoder.JSONDecodeError:
                films = []

        if not films:
            print("Фільмів немає")
            return

        print("=" * 100)
        for film in films:
            print(
                f"id:{film['id']}, "
                f"title:{film['title']}, "
                f"director:{film['director']}, "
                f"genre:{film['genre']}"
            )
        print("=" * 100)

        film_id = int(input("Введіть id фільму: "))

        selected_film = None

        for film in films:
            if film["id"] == film_id:
                selected_film = film
                break

        if selected_film is None:
            print("Такого фільму немає")
            return

        tickets = int(input("Введіть кількість квитків: "))

        if tickets <= 0:
            print("Кількість квитків повинна бути більше 0")
            return

        booking = {
            "film_id": selected_film["id"],
            "title": selected_film["title"],
            "tickets": tickets
        }

        if not Booking.booking_path.exists():
            with open(Booking.booking_path, "w", encoding="utf8") as f:
                json.dump([], f)

        with open(Booking.booking_path, "r+", encoding="utf8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []

            data.append(booking)

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

        print("Квитки успішно заброньовані")

    @staticmethod
    def show_bookings():
        if not Booking.booking_path.exists():
            print("Заброньованих квитків немає")
            return

        with open(Booking.booking_path, "r", encoding="utf8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                data = []

        if not data:
            print("Заброньованих квитків немає")
            return

        print("=" * 100)

        for booking in data:
            print(
                f"film id:{booking['film_id']}, "
                f"title:{booking['title']}, "
                f"tickets:{booking['tickets']}"
            )

        print("=" * 100)


Booking.book_ticket()
Booking.show_bookings()