from jinja2 import Environment, FileSystemLoader
from media_data import get_most_popular_movies


# Loads Templates dir to have acces to it.
env = Environment(loader=FileSystemLoader("templates/"))


def render(kwargs):
    """ Takes in a dict and return a rendered html. """
    template = env.get_template("template.html")
    return template.render(**kwargs)


class Movie():
    """ Takes in a dict for initialize. """
    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.description = kwargs.get("overview")
        self.image_url = kwargs.get("poster_path")
        self.trailer_id = kwargs.get("trailer_id")


def generate_movie_trailer():
    """ Fetch movies data and output a html file. """
    most_popular_movies = get_most_popular_movies()
    most_popular_movies = [Movie(**movie) for movie in most_popular_movies]
    with open("movie_trailer.html", "w", encoding="utf-8") as page:
        page.write(render(dict(movies=most_popular_movies)))


# In practice it's no necessary to create Movie instances,
# because jinja handle dicts as objects perced, so this
# function will be better.
# def generate_movie_trailer():
#     """ Fetch movies data and output a html file. """
#     most_popular_movies = get_most_popular_movies()
#     with open("movie_trailer.html", "w", encoding="utf-8") as page:
#         page.write(render(dict(movies=most_popular_movies)))


if __name__ == "__main__":
    generate_movie_trailer()
