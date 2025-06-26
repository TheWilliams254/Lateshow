from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date

db = SQLAlchemy()

class Appearance(db.Model):
    __tablename__ = 'appearances'
    
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete='CASCADE'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id', ondelete='CASCADE'), nullable=False)

    guest = db.relationship('Guest', back_populates='appearances')
    episode = db.relationship('Episode', back_populates='appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        return rating

    def __repr__(self):
        return f"<Appearance id={self.id} rating={self.rating} guest_id={self.guest_id} episode_id={self.episode_id}>"

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    occupation = db.Column(db.String(100))

    appearances = db.relationship('Appearance', back_populates='guest', cascade='all, delete-orphan')
    episodes = db.relationship(
        'Episode',
        secondary='appearances',
        back_populates='guests',
        overlaps="appearances,episode"
    )

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    def __repr__(self):
        return f"<Guest id={self.id} name={self.name}>"

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    show_date = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer)
    group = db.Column(db.String(50))

    appearances = db.relationship('Appearance', back_populates='episode', cascade='all, delete-orphan')
    guests = db.relationship(
        'Guest',
        secondary='appearances',
        back_populates='episodes',
        overlaps="appearances,guest"
    )

    @validates('show_date')
    def validate_show_date(self, key, show_date):
        if not show_date:
            raise ValueError("Show date cannot be empty")
        return show_date

    def __repr__(self):
        return f"<Episode id={self.id} show_date={self.show_date}>"
