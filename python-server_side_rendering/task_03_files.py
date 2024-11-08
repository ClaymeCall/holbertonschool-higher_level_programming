from flask import Flask, request, render_template
import json
import csv


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


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []

    if source == 'json':
        products = parse_json('products.json')
    elif source == 'csv':
        products = parse_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product_id = int(product_id)
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html')

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True , port=5000)
