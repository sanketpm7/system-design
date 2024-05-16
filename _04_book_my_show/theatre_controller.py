from Enums.city import City

from theatre import Theatre
from show import Show
from movie import Movie

class TheatreController:
    def __init__(self):
        self.city_vs_theatre: dict[City, list[Theatre]] = {}
        self.all_theatres: list[Theatre] = []
    
    def add_theatre(self, theatre: Theatre, city: City):
        self.all_theatres.append(theatre)

        cur_theatres = self.city_vs_theatre.get(city, [])
        cur_theatres.append(theatre)
        self.city_vs_theatre[city] = cur_theatres
    
    '''
        - get all shows (irrepective of theatre) 
        - let the result be int he form { theatre: [show1, show2, ....] }
    '''
    def get_all_show(self, movie: Movie, city: City) -> dict[Theatre, list[Show]]:
        if city not in self.city_vs_theatre:
            return []

        theatre_vs_shows = {}
        theatres = self.city_vs_theatre[city]

        # filter the theatres which run this movie
        for theatre in theatres:
            req_movie_shows = []
            shows = theatre.get_shows() 

            for show in shows:
                if show.get_movie().get_id == movie.get_id():
                    req_movie_shows.append(show)
            
            if req_movie_shows:
                theatre_vs_shows[theatre] = req_movie_shows
        
        return theatre_vs_shows