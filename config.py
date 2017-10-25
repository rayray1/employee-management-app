# import os

# Grabs the folder where the script runs.
# basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
# DEBUG = True

# DATABASE = 'spartan.db'
# USERNAME = 'admin'
# PASSWORD = 'admin'
# WTF_CSRF_ENABLED = True

# Secret key for session management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
# SECRET_KEY = 'my secret'

# define the full path for the database
#DATABASE_PATH = os.path.join(basedir, DATABASE)

# Connect to the database
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')


class Config(object):
    """Common configurations.
    """


class DevelopmentConfig(Config):
    """Development configurations.
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Production configurations.
    """

    DEBUG = False

app_config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}
