from app import db
from datetime import datetime

class repos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_name = db.Column(db.String)
    #file_name = db.Column(db.String)
    commit = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def __init__(self, repo_name, commit, timestamp):
        self.repo_name = repo_name
        self.commit = commit
        self.timestamp = timestamp


        