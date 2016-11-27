# MovieTrailerPages
A script to generate html files with most popular movies data.


#### Requirements

This script make use of jinja2 package for rendering
the html and request package for fetching the data.


You need Python 3.5 and pip, if installed just run:
``` pip install -r requirements.txt ```


#### How to use it?

First at all, as this script use the API from The Movie DB 
for fetching movies info, you are going to need a API Key.


Then go to `media_data.py` and place your API Key in 
`API_KEY = dict(api_key="The Movie DB Org API KEY")`,
replacing **The Movie DB Org API KEY** with your Key.


Finally just run `python movie_trailer.py`, it will generate 
a html file with the same name, open it and enjoy.
