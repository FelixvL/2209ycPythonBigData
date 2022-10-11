from flask import Flask
import mysql.connector
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = mysql.connector.connect(
    host = "bigdata-database.mysql.database.azure.com",
    port = "3306",
    user = "bigData",
    password = "qwer1234QWER!@#$",
    database = "skillapp"
    )

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE skillapp")
# mycursor.execute("CREATE TABLE users (ID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age int(3), endurance int(11), strength int(11), power int(11), speed int(11), flexibilty int(11), agility int(11), nerve int(11), durability int(11), hand_eye_co int(11), analytical_appr int(11))")

# db.commit()

print("Done!")


@app.route("/")
def index():
    return "hallo"

# When this URL is called, the function intro() will run
# The function intro() will create a new item in the database with the parameters given in the URL
# The function will return the id of the newly created user
# So when the URL is called, an id will be returned
@app.route("/intro/<vnaam>/<age>")
def intro(vnaam,age):
    # create new item in database, assign values name and age
    mycursor.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (vnaam, age))
    db.commit()
    # get corresponding id of new user from the database and assign it to variable id
    mycursor.execute("SELECT MAX(ID) FROM users")
    id = mycursor.fetchone()[0]
    print(id, vnaam, age, "added")
    # let this function return the id, so when this function is called you will get the id back
    return id

@app.route("/quiz/<speed>/<id>")
def quiz(speed, id):
    mycursor.execute("UPDATE users SET speed = '%s' WHERE ID = '%s'" % (speed, id))
    db.commit()
    print(speed, "added")
    return "beantwoord speed"

@app.route("/fits")
def fits():
    return 'fits.html'

@app.route("/home")
def home():
    return 'home.html'
