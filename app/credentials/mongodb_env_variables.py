import os
from dotenv import load_dotenv


load_dotenv()

mongo_user = os.getenv('MONGODB_USER')
mongo_pass = os.getenv('MONGODB_PASS')

print(mongo_user)
