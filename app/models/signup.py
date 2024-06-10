from app.extensions import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    user_type = db.Column(db.Integer)

    def __repr__(self):
        return f'<User "{self.name}">'