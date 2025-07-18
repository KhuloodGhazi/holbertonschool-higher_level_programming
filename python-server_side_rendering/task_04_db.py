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

@app.route('/')
def index():
    source = request.args.get('source')
    if source == 'json':
        products = get_data_from_json()
    elif source == 'csv':
        products = get_data_from_csv()
    elif source == 'sql':
        products = get_data_from_sql()
        if products is None:
            return render_template('product_display.html', products=[], error='Database error')
    else:
        return render_template('product_display.html', products=[], error='Wrong source')
    
    return render_template('product_display.html', products=products, error=None)

if __name__ == '__main__':
    app.run(debug=True)
