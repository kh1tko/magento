import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

base_url = config.get('urls', 'base_url')
login_url = config.get('urls', 'login_url')

username_qa = config.get('credentials', 'username')
password_qa = config.get('credentials', 'password')
