# server/schemas.py

from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from marshmallow import fields
from models import Customer, Item, Review

class ReviewSchema(SQLAlchemySchema):
    class Meta:
        model = Review
        load_instance = True

    id = auto_field()
    comment = auto_field()
    customer = fields.Nested('CustomerSchema', exclude=('reviews',))
    item = fields.Nested('ItemSchema', exclude=('reviews',))


class CustomerSchema(SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True

    id = auto_field()
    name = auto_field()
    email = auto_field()
    reviews = fields.Nested('ReviewSchema', many=True, exclude=('customer',))
    


class ItemSchema(SQLAlchemySchema):
    class Meta:
        model = Item
        load_instance = True

    id = auto_field()
    name = auto_field()
    price = auto_field()
    reviews = fields.Nested('ReviewSchema', many=True, exclude=('item',))
