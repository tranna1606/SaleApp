from models import Category, Product,User
import hashlib

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