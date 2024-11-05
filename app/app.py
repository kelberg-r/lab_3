from flask import Flask
from routes.main import main_bp
from routes.upload import upload_bp
from routes.view_data import view_data_bp
from routes.media import media_bp
from routes.products import products_bp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(view_data_bp)
app.register_blueprint(media_bp)
app.register_blueprint(products_bp)
if __name__ == '__main__':
    app.run(debug=True)
