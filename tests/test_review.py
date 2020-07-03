import unittest
from app.models import Review

class TestReview(unittest.TestCase):      

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(4, "nice", '/khsjha27hbs', "niceshow")

    def tearDown(self):
        Review.all_reviews = []

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))

    def test_save_review(self):
        self.new_review.save_review()
        self.assertEqual(len(Review.all_reviews), 1)

    def test_clear_reviews(self):
        self.new_review.clear_reviews()
        self.assertEqual(len(Review.all_reviews), 0)

    def test_get_reviews(self):
        self.new_review.save_review()
        found_review = Review.get_reviews(4)
        self.assertTrue(len(found_review) == 1)


    