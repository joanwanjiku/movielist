from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_movies, get_movie_by_id, get_movie_by_name, get_image_url
from ..models import Review
from .forms import ReviewForm



@main.route('/')
def index():
    title = 'Home'
    message = "I am happy to be here"
    search_movie = request.args.get('movie_query')
    print(search_movie)

    if search_movie:
        return redirect(url_for('.search_movie',movie_name=search_movie))
    else:
        return render_template('index.html', message=message, title=title)




@main.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = "MovieList"
    url = get_image_url()
    movie_result = get_movie_by_id(movie_id)
    reviews = Review.get_reviews(movie_id)
    message = "search result for %s" % movie_result.name
    return render_template('movie.html', message=message, title=title,url=url, result=movie_result, reviews= reviews)


@main.route('/popular')
def popular_movies():
    """
    on popular page to return popular movies
    """
    title = "Popular Movies"
    pop_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    showing_movies = get_movies('now_playing')
    url = get_image_url()
    # print(url)
    return render_template('popular.html', popular=pop_movies, title=title, url=url, upcoming=upcoming_movies, now_showing=showing_movies)


@main.route('/search/<movie_name>')
def search_movie(movie_name):
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


@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review_movie(id):
    form = ReviewForm()
    movie = get_movie_by_id(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.backdrop_path,review)
        new_review.save_review()
        return redirect(url_for('.movie',movie_id = movie.id ))

    title = f'{movie.name} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

