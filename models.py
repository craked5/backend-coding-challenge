from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
        # define here __repr__ and json methods or any common method
        # that you need for all your models

class Job(BaseModel):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    unbabel_id = db.Column(db.String)
    text = db.Column(db.String)
    state = db.Column(db.String)

    def __init__(self, unbabel_id, text, state):
        self.unbabel_id = unbabel_id
        self.text = text
        self.state = state

    def __repr__(self):
        return '<id {}>'.format(self.id)
