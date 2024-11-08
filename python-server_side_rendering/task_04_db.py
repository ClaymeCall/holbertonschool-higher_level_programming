from flask import Flask, request, render_template
import json
import csv
import sqlite3

app = Flask(__name__)

def parse_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def parse_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)

        # Populating product list with csv contents
        for row in reader:
            products.append(row)

    return products

def parse_sql_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = [
        {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    try:
        if source == 'json':
            products = parse_json('products.json')
        elif source == 'csv':
            products = parse_csv('products.csv')
        elif source == 'sql':
            products = parse_sql_db()
        else:
            return render_template('product_display.html', error="Wrong source")
        
        if product_id:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
    except Exception as e:
        return render_template('product_display.html', error=str(e))

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
