from flask import render_template
from app import app
from .requests import get_movies, get_movie_by_id, get_movie_by_name, get_image_url


@app.route('/')
def index():
    title = 'Home'
    message = "I am happy to be here"
    return render_template('index.html', message=message, title=title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = "MovieList"
    url = get_image_url()
    movie_result = get_movie_by_id(movie_id)
    message = "search result for %s" % movie_result.name
    return render_template('movie.html', message=message, title=title, result=movie_result, url=url)


@app.route('/popular')
def popular_movies():
    """
    on popular page to return popular movies
    """
    title = "Popular Movies"
    pop_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    showing_movies = get_movies('now_playing')
    print(showing_movies[2].backdrop_path)
    return render_template('popular.html', popular=pop_movies, title=title, upcoming=upcoming_movies, now_showing=showing_movies)


@app.route('/search/<movie_name>')
def search_movies(movie_name):
    """
    return the movies with the searched text
    """
    movie_name_list = movie_name.split(' ')
    new_movie_name = "+".join(movie_name_list)
    searched_movies = get_movie_by_name(new_movie_name)
    print(searched_movies[0].name)
    message = 'search results for %s' % movie_name.capitalize()
    title = 'Search'
    return render_template('search.html', results=searched_movies, message=message, title=title)

