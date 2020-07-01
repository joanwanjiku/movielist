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


