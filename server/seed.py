from models import db, Customer, Item, Review
from app import app

with app.app_context():
    db.create_all()

    c1 = Customer(name="Alice", email="alice@example.com")
    c2 = Customer(name="Bob", email="bob@example.com")

    i1 = Item(name="Backpack", price=49.99)
    i2 = Item(name="Thermos", price=19.99)

    r1 = Review(comment="Great quality!", customer=c1, item=i1)
    r2 = Review(comment="Very useful.", customer=c2, item=i1)
    r3 = Review(comment="Keeps drinks hot.", customer=c1, item=i2)

    db.session.add_all([c1, c2, i1, i2, r1, r2, r3])
    db.session.commit()
