from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

# Initialiser l'application Flask
app = Flask(__name__)
CORS(app)

# Charger le fichier JSON
with open('updated_products_data2.json', 'r') as f:
    products_data = json.load(f)

# Route pour obtenir tous les produits
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products_data)

# Route pour obtenir un produit par son nom
@app.route('/api/products/<string:name>', methods=['GET'])
def get_product_by_name(name):
    product = next((product for product in products_data if product['name'].lower() == name.lower()), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

# Route pour obtenir les produits best-sellers
@app.route('/api/products/best_sellers', methods=['GET'])
def get_best_sellers():
    best_sellers = [product for product in products_data if product['best_seller']]
    return jsonify(best_sellers)

# Route pour servir les images
@app.route('/images/<path:filename>', methods=['GET'])
def serve_image(filename):
    return send_from_directory(os.path.join(app.root_path, 'images'), filename)

# Démarrer l'application
if __name__ == '__main__':
    app.run(debug=True)
