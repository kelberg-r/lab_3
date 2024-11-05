from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from utils.db import get_db_connection

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/add', methods=['POST'])
def add_product():
    product_name = request.form.get('product_name')
    if not product_name:
        return jsonify({'error': 'Product name is required'}), 400
    
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO Products (product_name) VALUES (%s)", (product_name,))
        db.commit()
        print(f"Added product: {product_name}", flush=True)
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        db.close()
    
    return redirect(url_for('products.manage_products'))

@products_bp.route('/delete', methods=['POST'])
def delete_product():
    product_id = request.form.get('product_id')
    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400
    
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
        db.commit()
        print(f"Deleted product ID: {product_id}", flush=True)
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        db.close()
    
    return redirect(url_for('products.manage_products'))

@products_bp.route('/manage', methods=['GET'])
def manage_products():
    return render_template('manage_products.html')
