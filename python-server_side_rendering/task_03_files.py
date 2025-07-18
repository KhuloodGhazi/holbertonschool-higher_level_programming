from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv_data(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    error = None
    products = []

    json_path = os.path.join(app.root_path, 'products.json')
    csv_path = os.path.join(app.root_path, 'products.csv')

    if source == 'json':
        products = read_json_data(json_path)
    elif source == 'csv':
        products = read_csv_data(csv_path)
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p["id"] == product_id]
            if not filtered:
                error = "Product not found"
            else:
                products = filtered
        except ValueError:
            error = "Invalid ID format"
            products = []

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
