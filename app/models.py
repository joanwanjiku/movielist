class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.backdrop_path = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class Movie:
    """
    Contains attributes and behaviors of the object
    """
    def __init__(self, id_num, name, desc, img_url, rating, audience):
        """
        properties of the object
        """
        self.id = id_num
        self.name = name
        self.overview = desc
        self.backdrop_path = img_url
        self.vote_average = rating
        self.vote_count = audience


