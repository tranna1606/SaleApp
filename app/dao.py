from models import Category, Product,User
import hashlib
from app import app, db
from sqlalchemy import func

def get_categories():
    return Category.query.all()
def get_products(kw, cate_id):
    products = Product.query
    if kw:
       products = products.filter(Product.name.contains(kw))

    return products

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)

def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()


def count_products_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
                    .join(Product,Product.category_id.__eq__(Category.id))\
                    .group_by(Category.id).all()



def stats_revenue(kw):
    query = db.session.query(Product.id,Product.name, func.sum(ReceiptDetails.quantity*ReceiptDetails.price))\
                    .join(ReceiptDetails, ReceiptDetails.product_id.__eq__(Product.id))
    if kw:
        query = query.filter(Product.name.contains(kw))

    return query.group_by(Product.id).all()

def stats_revenue_by_month(year=2024):
    return db.session.query(func.extract('month',Receipt.created_date),func.sum(ReceiptDetails.quantity*ReceiptDetails.price))\
            .join(ReceiptDetails, ReceiptDetails.receipt_id.__eq__(Receipt.id)) \
            .filter(func.extract('year',Receipt.created_date).__eq__(year))\
            .group_by(func.extract('month',Receipt.created_date)).all()

if __name__=='__main__':
    with app.app_context():
        print(count_products_by_cate())