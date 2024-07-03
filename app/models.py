from .run import db

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
