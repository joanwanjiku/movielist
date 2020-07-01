class Config:
    MOVIE_API_KEY = 'b5c52c47ef50d43cdcf7ef93adebf4e9'

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/%s?api_key=%s'


class ProdConfig(Config):
    """
    subclass
    configurations for production environment inherits from Config
    """
    pass


class DevConfig(Config):
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True
