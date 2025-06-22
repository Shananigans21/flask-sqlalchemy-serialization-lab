from flask import Flask
from flask_migrate import Migrate
from models import db  # import the db instance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)           # Initialize SQLAlchemy with app
migrate = Migrate(app, db) # Setup Flask-Migrate

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
