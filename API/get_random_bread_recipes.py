import sqlite3

from flask import jsonify
import random

def get_random_recipes():
    conn = sqlite3.connect('D:\\Code kì 2\\bai tap cuoi ki\\instance\\bread.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM BREAD_RECIPES')
    bread_recipes = cursor.fetchall()
    conn.close()

    random_indexes = random.sample(range(0, len(bread_recipes)), 8)
    result = {}
    for i in range(len(random_indexes)):
        random_index = random_indexes[i]
        random_bread_recipe = bread_recipes[random_index]
        result.update({random_bread_recipe[2]: [random_bread_recipe[1], random_bread_recipe[3]]})
    
    return jsonify(result), 200


