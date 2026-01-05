from xml.etree.ElementInclude import default_loader

products = [
    {"name": "Apple", "category": "fruit", "price": 120, "quantity": 10},
    {"name": "Banana", "category": "fruit", "price": 90, "quantity": 15},
    {"name": "Avocado", "category": "fruit", "price": 200, "quantity": 5},
    {"name": "Tomato", "category": "veggie", "price": 100, "quantity": 20},
    {"name": "Broccoli", "category": "veggie", "price": 300, "quantity": 8},
    {"name": "Carrot", "category": "veggie", "price": 100, "quantity": 25},
    {"name": "Cookie", "category": "sweets", "price": 200, "quantity": 12, "brand": "ABC"},
    {"name": "Donut", "category": "sweets", "price": 300, "quantity": 7, "brand": "XYZ"},
    {"name": "Cake", "category": "sweets", "price": 400, "quantity": 3, "brand": "DEF", "discount": 10},
    {"name": "Orange", "category": "fruit", "price": 150, "quantity": 18},
    {"name": "Lettuce", "category": "veggie", "price": 80, "quantity": 30, "organic": True},
    {"name": "Chocolate", "category": "sweets", "price": 250, "quantity": 10, "brand": "GHI", "flavor": "Dark"}
]

# Пишите свой код ниже

def calculate_total_cost(list_products):
    total_cost = 0
    for product in list_products:
        try:
            price = product["price"]
            quantity = product["quantity"]
        except Exception:
            price = 0
            quantity = 0
        total_cost += price * quantity
    return total_cost

def filter_products_by_price(list_products, max_price):
    if list_products == [{}]:
        return list_products
    filtered_products = list_products.copy()
    for product in list_products:
        try:
            if product["price"] > max_price:
                filtered_products.pop(filtered_products.index(product))
        except Exception:
            filtered_products.pop(filtered_products.index(product))
    return filtered_products

def find_product_by_name(list_products, name):
    for product in list_products:
        try:
            if product["name"] == name:
                return product
        except Exception:
            pass
    return "Продукт с таким именем не найден в списке"

def update_product_info(list_products, name_product_to_update, update_info):
    flag = True
    for product in list_products:
        try:
            if product["name"] == name_product_to_update:
                flag = False
                for key, value in update_info.items():
                    list_products[list_products.index(product)][key] = value
        except Exception:
            pass
    if flag:
        return "Продукт с таким именем не найден в списке"
    return list_products

def sort_products_by_quantity(list_products, ascending=False):
    if ascending:
        for i in range(len(list_products)-1):
            for j in range(len(list_products)-i-1):
                first = list_products[j].get("quantity") if isinstance(list_products[j].get("quantity"), int) else 0
                second = list_products[j + 1].get("quantity") if isinstance(list_products[j + 1].get("quantity"), int) else 0
                if(first < second):
                    swap_products(j, list_products)
    else:
        for i in range(len(list_products)-1):
            for j in range(len(list_products)-i-1):
                first = list_products[j].get("quantity") if isinstance(list_products[j].get("quantity"), int) else 0
                second = list_products[j + 1].get("quantity") if isinstance(list_products[j + 1].get("quantity"), int) else 0
                if(first > second):
                    swap_products(j, list_products)
    return list_products


def swap_products(index: int, list_products):
    buf = list_products[index]
    list_products[index] = list_products[index + 1]
    list_products[index + 1] = buf

def average_price_per_category(list_products):
    result = {}
    count = {}
    try:
        for product in list_products:
            if product["category"] in result.keys():
                result[product["category"]] += product["price"]
                count[product["category"]] += 1
            else:
                result[product["category"]] = product["price"]
                count[product["category"]] = 1
        for category in result.keys():
            result[category] = round(result[category] / count[category], 1)
        return result
    except Exception:
        return result


def group_products_by_category(products):
    result = {}
    for product in products:
        try:
            if product["category"] in result.keys():
                result[product["category"]].append(product)
            else:
                result[product["category"]] = [product]
        except Exception:
            pass
    return result



grouped_by_category = group_products_by_category(products)
for group in grouped_by_category:
    print(group)
    for product in grouped_by_category[group]:
        print(product)