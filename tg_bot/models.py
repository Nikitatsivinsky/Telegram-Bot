from tg_bot import db
import uuid

from sqlalchemy import text


# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()

class Application(db.Model):
    __tablename__ = 'application'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class Brand(db.Model):
    __tablename__ = 'brand'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class SubCategory(db.Model):
    __tablename__ = 'subcategory'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    item_id = db.Column(db.String, db.ForeignKey('items.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='subcategories')


def __repr__(self):
        return self.name


class Color(db.Model):
    __tablename__ = 'color'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class Gender(db.Model):
    __tablename__ = 'gender'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return self.name


class Material(db.Model):
    __tablename__ = 'material'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class Size(db.Model):
    __tablename__ = 'size'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Numeric(3, 1), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Item(db.Model):
    """
    For UUID used uuid_generate_v4(), for install this function in Data Base, you need open terminal
    >sudo -u postgres psql
    >CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    """

    __tablename__ = 'items'

    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), server_default=text("uuid_generate_v4()"))
    name = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    applications = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    subcategory = db.relationship('SubCategory',  primaryjoin="Item.id==SubCategory.item_id", backref='item')
    colors = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    gender = db.Column(db.Integer, db.ForeignKey('gender.id'), nullable=False)
    materials = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    types = db.Column(db.Integer, db.ForeignKey('type.id'), nullable=False)
    image = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    famous = db.Column(db.Integer, nullable=True)
    in_stock = db.Column(db.Integer, nullable=False)
    length_cm = db.Column(db.SmallInteger, nullable=True)
    price = db.Column(db.Numeric(scale=2, precision=8), nullable=True)
    discount = db.Column(db.Numeric(scale=2, precision=8), nullable=True)
    size = db.Column(db.Integer, db.ForeignKey('size.id'), nullable=False)
    weight = db.Column(db.Integer())
    year = db.Column(db.Integer())

    def __repr__(self):
        return str(f'{self.name} {self.model}')



class MainBanner(db.Model):
    __tablename__ = 'main_banner'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref=db.backref('main_banner', uselist=False), lazy=True)

class NewesBanner(db.Model):
    __tablename__ = 'newes_banner'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref=db.backref('newes_banner', uselist=False), lazy=True)

    def __repr__(self):
        return f"<NewesBanner {self.item.name}>"



class SaleBanner(db.Model):
    __tablename__ = 'salebanner'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref=db.backref('sale_banner', uselist=False), lazy=True)

    def __repr__(self):
        return str(self.subject)


class ExclusiveBanner(db.Model):
    __tablename__ = 'exclusivebanner'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref=db.backref('exclusive_banner', uselist=False), lazy=True)

    def __repr__(self):
        return str(self.subject)


class PopularBanner(db.Model):
    __tablename__ = 'popularbanner'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    item = db.relationship('Item', backref=db.backref('popular_banner', uselist=False), lazy=True)

    def __repr__(self):
        return str(self.subject)


# # AUTH

class Profile(db.Model):
    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.Integer)
    user = db.Column(db.String(50))
    login = db.Column(db.String(50))
    password = db.Column(db.String(50))
    telephone = db.Column(db.String(20), nullable=True)
    country = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(20), nullable=True)
    adress = db.Column(db.String(20), nullable=True)
    zip_code = db.Column(db.String(20), nullable=True)
    birth_date = db.Column(db.DateTime(), nullable=True)
    photo = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        return str(self.user)


class MailDistribution(db.Model):
    __tablename__ = 'maildistribution'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.email


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    cart = db.relationship('Cart', primaryjoin="Order.id==Cart.order_id", backref='order', lazy=True)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    comment = db.Column(db.String(255), nullable=True)
    ttn = db.Column(db.Numeric(14), nullable=True)

    def __repr__(self):
        return str(self.id)


class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    item_id = db.Column(db.String(36), db.ForeignKey('items.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def __repr__(self):
        return str(self.id)
