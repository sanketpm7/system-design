from Enums.city import City
from movie import Movie

class MovieController:
    def __init__(self):
        self.city_vs_movies: dict[City, list[Movie]] = {}
        self.all_movies: list[Movie] = []
    
    '''
    # use both `all_movies` & `city_vs_movies`
        add_movie() - to a city
        remove_movie() - from a city
        update_movie() - of a city
        delete_movie() - from a city

    # use `all_movies`
        get_movie_by_name()
        get_movie_by_id()

    # use `city_vs_movies`
        get_movie_by_city()
    '''
    def add_movie(self, movie: Movie, city: City):
        self.all_movies.append(movie)

        cur_movies = self.city_vs_movies.get(city, [])
        cur_movies.append(movie)
        
        self.city_vs_movies[city] = cur_movies
    
    def remove_movie(self):
        pass
    
    def get_movie_by_name(self, name) -> Movie:
        for movie in self.all_movies:
            if movie.get_name() == name:
                return movie
        return None
    
    def get_movies_by_city(self, city: City) -> list[Movie]:
        return self.city_vs_movies[city]