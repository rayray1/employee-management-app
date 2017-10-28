# instance/config.py
import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


SECRET_KEY = 'mysecretkeyhere'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
