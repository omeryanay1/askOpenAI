from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import ask_view

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@flask_db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
db.create_all()
ask_view(app)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
