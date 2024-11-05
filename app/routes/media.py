from flask import Blueprint, render_template, jsonify, send_from_directory
import os
from utils.db import get_db_connection

media_bp = Blueprint('media', __name__, url_prefix='/media')

@media_bp.route('/by_product/<int:product_id>', methods=['GET'])
def get_media_by_product(product_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT media_id, media_type, media_path
            FROM MediaContent
            WHERE product_id = %s
        """, (product_id,))
        media_files = cursor.fetchall()
        print(f"Media files fetched: {media_files}", flush=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        db.close()

    return jsonify(media_files)

@media_bp.route('/file/<filename>')
def display_media(filename):
    directory_path = os.path.join(os.getcwd(), 'uploads')
    print(f"Trying to serve file from: {directory_path}{filename}", flush=True)
    if not os.path.exists(os.path.join(directory_path, filename)):
        print("File not found!", flush=True)
        return "File not found", 404
    return send_from_directory(directory_path, filename)

@media_bp.route('/view')
def view_media_page():
    return render_template('view_media.html')
