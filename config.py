import os

class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/%s?api_key=%s'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

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


config_options = {
'development':DevConfig,
'production':ProdConfig
}
