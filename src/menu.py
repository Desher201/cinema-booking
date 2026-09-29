from movies import Movie
from booking import Booking

while True:
    print("1] Перегляд фільмів\n"
          "2] Бронювання\n"
          "3] Обрані фільми\n"
          "4] Вихід\n")
    choice = int(input())
    if choice == 1:
        Movie.show_all_films()
    if choice == 2:
        Booking.book_ticket()
    if choice == 3:
        Booking.show_bookings()
    if choice == 4:
        break