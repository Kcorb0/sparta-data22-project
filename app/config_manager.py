import configparser
from app.definitions import PROJECT_ROOT_DIR
import os

_config = configparser.ConfigParser()
PROJECT_PATHWAY = os.path.join(PROJECT_ROOT_DIR, 'config.ini')
_config.read(PROJECT_PATHWAY)

AWS_BUCKET_NAME = _config['aws']['bucket_name']


# Last second removal as changing to .env file added to gitignore
# MONGO_USERNAME = _config['mongodb']['username']
# MONGO_PASSWORD = _config['mongodb']['password']
