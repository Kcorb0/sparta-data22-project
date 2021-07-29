import os
from dotenv import load_dotenv

def grab_credentials():
    env_path = f'{os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))}\\.env.txt'
    load_dotenv(env_path)