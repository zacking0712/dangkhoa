def load_categories():
    return [{
        'id': 1.,
        'name': 'Mobile'
    },{
        'id': 2.,
        'name': 'Tablet'
    },{
        'id': 3.,
        'name': 'Laptop'
    }]

def load_products(kw):
    products = [{
        'name': 'Iphone 15',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    },{
        'name': 'Iphone 14',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    },{
        'name': 'Iphone 13',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    },{
        'name': 'Laptop ',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    },{
        'name': 'Tablet 14',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    },{
        'name': 'Samsung',
        'price': 2000000,
        'image' : "https://cdn.tgdd.vn/Products/Images/1363/291962/mieng-dan-man-hinh-iphone-14-pro-ub-1.jpg"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products