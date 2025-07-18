from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_data_from_json():
    with open('products.json') as f:
        return json.load(f)

def get_data_from_csv():
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        return list(reader)

def get_data_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        return [
            {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            } for row in rows
        ]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

@app.route('/products')
def index():
    source = request.args.get('source')
    product_id = request.args.get('id')
    products = []
    error = None

    if source == 'json':
        products = get_data_from_json()
    elif source == 'csv':
        products = get_data_from_csv()
    elif source == 'sql':
        products = get_data_from_sql()
        if products is None:
            error = 'Database error'
    else:
        error = 'Wrong source'

    # Filter by product_id if provided and no previous error
    if error is None and product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if int(p['id']) == product_id]
            if filtered:
                products = filtered
            else:
                products = []
                error = 'Product not found'
        except ValueError:
            products = []
            error = 'Invalid ID format'

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True)
