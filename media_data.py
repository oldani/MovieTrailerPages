import requests


API_KEY = dict(api_key="The Movie DB Org API KEY")
API_URL = "https://api.themoviedb.org/3/"


def get_movie_trailer(movie):
    """ Recive a movie dict, take de id and return de same object with a
        YouTube trailer video key. """
    movie_id = movie.get("id")
    movie_videos_url = "".join([API_URL, "movie/{}/videos".format(movie_id)])
    response = requests.get(movie_videos_url, params=API_KEY)
    video = response.json().get("results")[0]
    movie["trailer_id"] = video.get("key")
    return movie


def get_most_popular_movies():
    """ Return a list of 15 most popular movies info. """
    most_popular_url = ''.join([API_URL, "movie/popular"])
    response = requests.get(most_popular_url, params=API_KEY)
    response_results = response.json().get("results")
    return [get_movie_trailer(movie) for movie in response_results[:15]]
