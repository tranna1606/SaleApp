def get_categories():
    return [{
        "id":1,
        "name":"Mobile"
    },{
        "id":2,
        "name":"Tablet"
    }]

def get_products(kw):
    products =[{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    },{
        "id":2,
        "name":"Galaxy S23 Plus",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    },{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    },{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    },{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    },{
        "id":1,
        "name":"iPhone13",
        "price":20000000,
        "image":"https://www.itworld.com.my/image/cache/catalog/Images/Smartphone/PHOAPPLMQ9T3ZP_T1-1000x1000.png",
        "category_id":1
    }]
    if kw:
       products =[p for p in products if p['name'].lower().find(kw.lower()) >=0]

    return products