import pytest
from app import app
from models import db  # Explicit import for db

@pytest.fixture(scope="function")
def test_client():
    app.config["TESTING"] = True
    app.config["DEBUG"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    with app.app_context():
        db.create_all()
        db.session.commit()

        with app.test_client() as client:
            yield client

        db.session.remove()
        db.drop_all()
