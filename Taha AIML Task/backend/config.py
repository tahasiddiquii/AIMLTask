import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:root@localhost/tahadb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
