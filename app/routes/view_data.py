from flask import Blueprint, render_template, jsonify
from utils.db import get_db_connection

view_data_bp = Blueprint('view_data', __name__)

@view_data_bp.route('/view_data')
def view_data():
    return render_template('view_data.html')

@view_data_bp.route('/view_table/<table_name>', methods=['GET'])
def view_table(table_name):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        valid_tables = ['Resources', 'Products', 'Orders', 'OrderDetails', 'TechMap', 'Sales', 'SaleDetails']
        if table_name not in valid_tables:
            return jsonify({'error': 'Invalid table name'}), 400

        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    return jsonify(data)
