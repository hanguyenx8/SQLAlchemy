from saleapp import db, app

from models import Category, product_tag, Product, Tag

import warnings
warnings.filterwarnings("ignore")

app.app_context().push()
if __name__ == "__main__":
    #c1 = Category(name = "Mobile")
    #c2 = Category(name = "Tablet")
    #c3 = Category(name = "Desktop")
    #c4 = Category(name = "clother")
    #t1 = Tag(name = "new")
    #t2 = Tag(name = "sale_off_30%")
    #p1 = Product(name="Iphone 7 Plus", price = 12, category_id = 1)
    #p2 = Product(name="Iphone 13 Promax", price = 17, description ="Apple", category_id = 1)
    #p3 = Product(name="Ipad Pro 2021", price = 34, description ="Apple", category_id = 2)
    #p4 = Product(name="Galaxy S23", price = 20, description ="Samsung", category_id = 4)
    #db.session.add(c1)
    #db.session.add(c2)
    #db.session.add(c3)
    #db.session.add(c4)
    #db.session.commit()
    #db.session.add(t1)
    #db.session.add(t2)
    #db.session.commit()
    #db.session.add(p1)
    #db.session.add(p2)
    #db.session.add(p3)
    #db.session.add(p4)
    t1 = db.session.query(Tag).get(1)
    t2 = db.session.query(Tag).get(2)
    p = db.session.query(Product).get(6)
    p.tags.append(t1)
    p.tags.append(t2)
    db.session.add(p)
    db.session.commit() 