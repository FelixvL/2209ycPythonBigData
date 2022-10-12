from flask import Flask
import mysql.connector
from flask_cors import CORS, cross_origin
import collections

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
# @app.route("/intro/<vnaam>/<age>")
# def intro(vnaam,age):
#     # create new item in database, assign values name and age
#     mycursor.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (vnaam, age))
#     db.commit()
#     # get corresponding id of new user from the database and assign it to variable id
#     mycursor.execute("SELECT MAX(ID) FROM users")
#     id = mycursor.fetchone()[0]
#     print(id, vnaam, age, "added")
#     # let this function return the id, so when this function is called you will get the id back
#     return str(id)

# @app.route("/quiz/<speed>/<id>")
# def quiz(speed, id):
#     mycursor.execute("UPDATE users SET speed = '%s' WHERE ID = '%s'" % (speed, id))
#     db.commit()
#     print(speed, "added!")
#     return "beantwoord speed"

@app.route("/fits/<id>")
def generated(id):
    mycursor = db.cursor(buffered=True)
    mycursor.execute("SELECT endurance,strength,power,speed,agility,flexibility,nerve,durability,handeyecoordination,analyticalaptitude FROM users WHERE ID = 77")
    value_user = mycursor.fetchone()
    value_user = list(value_user)
    db.commit()
    print(value_user)

    def waarde_bepalen(z):
        total_list_user = []
        skill_lijst_lp = ["endurance", "strength", "power", "speed", "agility", "flexibility", "nerve", "durability", "handeyecoordination", "analyticalaptitude"]
        for x in z():
            for skill in skill_lijst_lp:
                skill_list = skill + "_" + x
                total_list_user.append(globals()[skill_list])  
        total_list_user = [item for sublist in total_list_user for item in sublist]
        counted_sports = collections.Counter(total_list_user).most_common()
        top_3_sports = counted_sports[0:3]
        top_10_sports = counted_sports[0:10]    
        sport1 = "".join(top_3_sports[0][0])
        sport2 = "".join(top_3_sports[1][0])
        sport3 = "".join(top_3_sports[2][0])  
        print("1.", sport1)
        print("2.", sport2)
        print("3.", sport3)
        print(top_10_sports)   
        return "top_3_sports"

    waarde_bepalen(value_user)

    return "rij_gebruiker"

@app.route("/fits/<country>/<education>/<job>/<email>/<password>")
def fits(country, education, job, email, password):
    mycursor.execute("UPDATE users SET country = '%s', education = '%s', job = '%s', email = '%s', password = '%s' WHERE ID = %s" % (country, education, job, email, password, 78))
    db.commit()
    print("fits added!")
    return 'fits.html'
