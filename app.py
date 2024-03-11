from flask import *
from database_interact import *
from create_database import create_database
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from python_classes.user import User
from python_classes.wine import Wine

app = Flask(__name__)

###???
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)
###???

# create_database()
db = sqlite3.connect("databse.db")
@app.route('/')
def index():
    return render_template('index.html')

### як зробити так, щоб воно поверталось на "/"
@app.route('/index.html')
def home():
    return render_template('index.html')
###

@app.route('/map_of_wines.html')
def map_of_wines():
    return render_template('map_of_wines.html')

@app.route('/info_best_for.html')
def etiquette():
    return render_template('info_best_for.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        ###як перевіряти, чи павильний пароль?
        user_email = request.form['email']
        user_password = request.form['password']
        new_user = User(user_email, user_password)
        add_new_user(new_user)
        return 'Hello'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)