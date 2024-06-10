from app.extensions import db

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    user_type = db.Column(db.Integer)

# from app.extensions import db
# from app.models.User import User
# db.create_all()

# Test `user_adm = User(id="123007", name="Daniela", email="dani@mail.com", password="dani123", user_type=1)`
# user_adm, user_adm.name

# db.session.add(user_adm)
# db.session.commit()   