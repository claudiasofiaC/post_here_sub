"""This is my database models"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    username = DB.Column(DB.Text(), nullable=False, primary_key=True)
    password = DB.Column(DB.Text(), nullable=False)
    session_key = DB.Column(DB.Text())

class Post(DB.Model):
    article = DB.Column(DB.Text(), nullable=False)
    subreddit = DB.Column(DB.Text(), nullable=False)
    author = DB.Column(DB.Text(), nullable=False)
    post_id = DB.Column(DB.Integer(), primary_key=True)
    saved = DB.Column(DB.Integer(), nullable=False)
