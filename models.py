from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from saleapp import db, app


class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='Category', lazy=True)

product_tag = db.Table('product_tag',
            Column('product_id', Integer, ForeignKey('product.id'), primary_key=True),
            Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
            )

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), default="None description")
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(255))
    created_date = Column(DateTime, default= datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    tags = relationship('Tag', secondary='product_tag', lazy="subquery",
                      backref=backref('products', lazy = True))


class Tag(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


app.app_context().push()
if __name__ == "__main__":
    db.create_all()

