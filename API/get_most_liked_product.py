import sqlite3
from flask import jsonify

def get_most_liked_products():
    conn = sqlite3.connect('D:\\Code kì 2\\bai tap cuoi ki\\instance\\bread.db')
    cursor = conn.cursor()

    cursor.execute('select * from product order by like desc')
    most_liked_products = cursor.fetchall()
    conn.close()

    most_liked_products = most_liked_products[:8]

    result = {}
    for i in range(len(most_liked_products)):
        product = most_liked_products[i]
        result.update({product[1]: [product[2], product[3]]})
    return jsonify(result), 200