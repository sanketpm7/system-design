from book_my_show import BookMyShow

class Main:
    def __init__(self):
        book_my_show = BookMyShow()
        book_my_show.create_booking('city', 'movie_name')


if __name__ == '__main__':
    main = Main()
