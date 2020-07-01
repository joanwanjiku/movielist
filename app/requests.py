from app import app
import urllib.request
import json
from .models.movie import Movie

# get the apikey
api_key = app.config['MOVIE_API_KEY']
# get the movie base url
base_url = app.config['MOVIE_API_BASE_URL']


def get_movies(category):
    """
    gets the response from our api call
    """
    get_movies_url = base_url % (category, api_key)
    # print(get_movies_url)

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None
        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)
    return movie_results


def process_results(movie_list):
    movie_results = []
    for movie_item in movie_list:
        movie_id = movie_item.get('id')
        movie_name = movie_item.get('title')
        movie_overview = movie_item.get('overview')
        movie_backdrop_path = movie_item.get('backdrop_path')
        movie_vote_average = movie_item.get('vote_average')
        movie_vote_count = movie_item.get('vote_count')

        movie_object = Movie(movie_id, movie_name, movie_overview, movie_backdrop_path, movie_vote_average, movie_vote_count)
        movie_results.append(movie_object)
    return movie_results


def get_movie_by_name(movie_name):
    search_url = 'https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s' % (api_key, movie_name)
    with urllib.request.urlopen(search_url) as url:
        get_search_data = url.read()
        get_movie_result = json.loads(get_search_data)

        processed_results = None
        if get_movie_result['results']:
            search_movie_list = get_movie_result['results']
            processed_results = process_results(search_movie_list)
    return processed_results

def get_movie_by_id(movie_id):
    """
    searches for a movie with the passed in id
    :param movie_id:
    :return: a movie object
    """
    search_url = 'https://api.themoviedb.org/3/movie/%s?api_key=%s' %(movie_id, api_key)
    with urllib.request.urlopen(search_url) as url:
        get_movie_data = url.read()
        get_movie_result = json.loads(get_movie_data)

        movie_idnum = get_movie_result.get('id')
        movie_name = get_movie_result.get('original_title')
        movie_overview = get_movie_result.get('overview')
        movie_backdrop = get_movie_result.get('backdrop_path')
        movie_average = get_movie_result.get('vote_average')
        movie_count = get_movie_result.get('vote_count')

        movie_object = Movie(movie_id, movie_name, movie_overview, movie_backdrop, movie_average, movie_count)

    return movie_object

def get_image_url():
    search_url = 'https://api.themoviedb.org/3/configuration?api_key=%s' % api_key
    with urllib.request.urlopen(search_url) as url:
        get_urls = url.read()
        get_url_result = json.loads(get_urls)

        base_url = get_url_result.get('images')

        url = get_url_result['images']['base_url'] + get_url_result['images']['backdrop_sizes'][1]
    # print(url)
    return url







