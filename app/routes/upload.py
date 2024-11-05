from flask import Blueprint, request, redirect, url_for, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from utils.db import get_db_connection

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files or 'product_id' not in request.form:
            return jsonify({'error': 'No file or product ID provided'}), 400
        
        file = request.files['file']
        product_id = request.form['product_id']
        
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join('uploads/', filename)
            file.save(file_path)
            
            # Save only the filename to the database
            db = get_db_connection()
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO MediaContent (product_id, media_type, media_path)
                VALUES (%s, %s, %s)
            """, (product_id, file.mimetype, filename))
            db.commit()
            cursor.close()
            db.close()
            
            return redirect(url_for('upload.upload'))
    return render_template('upload.html')
