from tg_bot import db
import uuid
from sqlalchemy.dialects.postgresql import UUID


# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()


class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name


class Brand(db.Model):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name


class SubCategory(db.Model):
    __tablename__ = 'subcategories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    parent = db.relationship('Category', backref=db.backref('category_subcategory', uselist=False), lazy=True)

    def __repr__(self):
        return self.name


class Color(db.Model):
    __tablename__ = 'colors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name


class Gender(db.Model):
    __tablename__ = 'genders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return self.name


class Material(db.Model):
    __tablename__ = 'materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name


class Type(db.Model):
    __tablename__ = 'types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return self.name


class Size(db.Model):
    __tablename__ = 'sizes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Numeric(3, 1))

    def __repr__(self):
        return self.name


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(50))
    model = db.Column(db.String(50), nullable=True)
    brand = db.relationship('Brand', backref='brands_item', lazy=True)
    applications = db.relationship('Application', backref='application_item', lazy=True)
    category = db.relationship('Category', backref='category_item', lazy=True)
    subcategory = db.relationship('SubCategory', backref='subcategory_item', lazy=True)
    colors = db.relationship('Color', backref='color_item', lazy=True)
    gender = db.relationship('Gender', backref='gender_item', lazy=True)
    materials = db.relationship('Material', backref='material_item', lazy=True)
    types = db.relationship('Type', backref='types_item', lazy=True)
    image = db.Column(db.String(50))
    description = db.Column(db.Text)
    famous = db.Column(db.SmallInteger)
    in_stock = db.Column(db.SmallInteger)
    length_cm = db.Column(db.SmallInteger, nullable=True)
    price = db.Column(db.Numeric(scale=2, precision=8))
    discount = db.Column(db.Numeric(scale=2, precision=8), nullable=True)
    size = db.relationship('Size', backref='size_item', lazy=True)
    weight = db.Column(db.Integer())
    year = db.Column(db.Integer())

    def __repr__(self):
        return str(f'{self.name} {self.model}')


class MainBanner(db.Model):
    __tablename__ = 'mainbanners'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.relationship('Item', backref='main_banner', lazy=True)

    def __repr__(self):
        return str(self.subject)


class NewesBanner(db.Model):
    __tablename__ = 'newesbanners'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.relationship('Item', backref='newes_banner', lazy=True)

    def __repr__(self):
        return str(self.subject)


class SaleBanner(db.Model):
    __tablename__ = 'salebanners'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.relationship('Item', backref='sale_banner', lazy=True)

    def __repr__(self):
        return str(self.subject)


class ExclusiveBanner(db.Model):
    __tablename__ = 'exclusivebanners'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.relationship('Item', backref='exclusive_banner', lazy=True)

    def __repr__(self):
        return str(self.subject)


class PopularBanner(db.Model):
    __tablename__ = 'popularbanners'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.relationship('Item', backref='popular_banner', lazy=True)

    def __repr__(self):
        return str(self.subject)


# AUTH

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
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
    __tablename__ = 'maildistributions'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return self.email


class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='user_cart', lazy=True)
    item = db.relationship('Item', backref='item_cart', lazy=True)
    quantity = db.Column(db.Integer, default=1)
    __table_args__ = (
        db.CheckConstraint('quantity > 0'),
    )

    def __repr__(self):
        return str(self.id)


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='user_order', lazy=True)
    cart = db.relationship('Cart', backref='cart_order', lazy=True)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    comment = db.Column(db.String(255), nullable=True)
    ttn = db.Column(db.Integer())

    def __repr__(self):
        return str(self.id)
