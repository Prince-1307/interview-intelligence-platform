from flask import Flask
from routes.home import home_bp
from routes.upload import upload_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(upload_bp)


if __name__ == "__main__":

    app.run(debug=True)