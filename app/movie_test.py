import unittest
from .models.movie import Movie


class MovieTest(unittest.TestCase):
    """
    Test the behavior of class Movie
    """
    def setUp(self):
        """
        Runs before each testcase
        """
        self.new_movie = Movie(1, "Python", "About python the animal not programming language", "https://image.tmdb.org/t/p/w500/nlCHUWjY9XWbuEUQauCBgnY8ymF.jpg", 8.5, 129653 )

    def test_init(self):
        """
        checks to see if object is initialized properly
        """
        self.assertEqual(self.new_movie.id, 1)
        self.assertEqual(self.new_movie.name, "Python")
        self.assertEqual(self.new_movie.overview, "About python the animal not programming language")
        self.assertEqual(self.new_movie.backdrop_path, "https://image.tmdb.org/t/p/w500/nlCHUWjY9XWbuEUQauCBgnY8ymF.jpg")
        self.assertEqual(self.new_movie.vote_average, 8.5)
        self.assertEqual(self.new_movie.vote_count, 129653)


