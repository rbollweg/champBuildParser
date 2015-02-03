__author__ = 'The Gibs'

from app import db

class Match(db.Model):
    __tablename__ = "matches"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    date_play = db.Column(db.DateTime)
    builds = db.relationship('Build', backref='match', lazy='dynamic')

    def __init__(self, url, date_play):
        self.url = url
        self.date_play = date_play


class Build(db.Model):
    __tablename__ = "builds"

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'))
    champ_name = db.Column(db.String)
    steps = db.relationship('Step', backref='build', lazy='dynamic')

class Step(db.Model):
    __tablename__ = "steps"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String)
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
    items = db.relationship('Item', backref='step', lazy='dynamic')

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    step_id = db.Column(db.Integer, db.ForeignKey('steps.id'))
    is_sold = db.Column(db.Boolean)
    item = db.Column(db.String)






