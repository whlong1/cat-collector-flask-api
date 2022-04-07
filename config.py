import os

DATABASE_URL = os.getenv('DATABASE_URL')

class Config:
  CORS_HEADERS = 'Content-Type'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  if DATABASE_URL:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)
  else:
    DEBUG=True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5432/cat_collector_api"