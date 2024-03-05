from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    """Connect to the database"""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class User(db.Model):
    """Model for user"""

    __tablename__ = 'users'

    username = db.Column(
        db.String(20),
        primary_key=True
    )

    hashed_password = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    first_name = db.Column(
        db.String(30),
        nullable=False
    )

    last_name = db.Column(
        db.String(30),
        nullable=False
    )

    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """ Register new user with hashed password and user info """

        hashed = bcrypt.generate_password_hash(pwd).decode('utf8')

        return cls(
            username=username,
            hashed_password=hashed,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
