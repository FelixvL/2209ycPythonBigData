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

# @app.route("/")
# def index():
#     return "hallo"

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
    return str(id)


@app.route("/fits/<id>")
def generated(id):
    mycursor = db.cursor(buffered=True)
    mycursor.execute("SELECT endurance,strength,power,speed,agility,flexibility,nerve,durability,handeyecoordination,analyticalaptitude FROM users WHERE ID = 77")
    value_user = mycursor.fetchone()
    value_user = [*value_user]
    db.commit()
    print(value_user)

    endurance_beg = ['Track and Field: Pole Vault', 'Bobsledding/Luge', 'Ski Jumping', 'Track and Field: High Jump', 'Diving', 'Track and Field: Sprints', 'Rodeo: Calf Roping', 'Rodeo: Bull/Bareback/Bronc Riding', 'Table Tennis', 'Track and Field: Weights', 'Golf', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    endurance_mid = ['Football', 'Wrestling', 'Martial Arts', 'Gymnastics', 'Baseball/Softball', 'Skiing: Alpine', 'Lacrosse', 'Rodeo: Steer Wrestling', 'Figure Skating', 'Volleyball', 'Racquetball/Squash', 'Surfing', 'Fencing', 'Skiing: Freestyle', 'Team Handball', 'Cycling: Sprints', 'Badminton', 'Auto Racing', 'Track and Field: Long, Triple jumps', 'Skateboarding', 'Track and Field: Middle Distance', 'Weight-Lifting', 'Swimming (all strokes): Sprints', 'Water Skiing', 'Horse Racing', 'Cheerleading', 'Roller Skating']
    endurance_pro = ['Boxing', 'Ice Hockey', 'Basketball', 'Tennis', 'Soccer', 'Water Polo', 'Rugby', 'Field Hockey', 'Speed Skating', 'Cycling: Distance', 'Skiing: Nordic', 'Swimming (all strokes): Distance', 'Rowing', 'Track and Field: Distance', 'Canoe/Kayak']

    strength_beg = ['Racquetball/Squash', 'Fencing', 'Team Handball', 'Badminton', 'Auto Racing', 'Skateboarding', 'Table Tennis', 'Horse Racing', 'Golf', 'Cheerleading', 'Roller Skating', 'Equestrian', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    strength_mid = ['Martial Arts', 'Tennis', 'Baseball/Softball', 'Soccer', 'Skiing: Alpine', 'Lacrosse', 'Field Hockey', 'Figure Skating', 'Volleyball', 'Surfing', 'Skiing: Freestyle', 'Bobsledding/Luge', 'Ski Jumping', 'Skiing: Nordic', 'Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Diving', 'Swimming (all strokes): Distance', 'Track and Field: Sprints', 'Rodeo: Calf Roping', 'Track and Field: Distance', 'Rodeo: Bull/Bareback/Bronc Riding', 'Track and Field: Middle Distance', 'Swimming (all strokes): Sprints', 'Water Skiing', 'Canoe/Kayak', 'Archery']
    strength_pro = ['Boxing', 'Ice Hockey', 'Football', 'Basketball', 'Wrestling', 'Gymnastics', 'Water Polo', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Speed Skating', 'Cycling: Distance', 'Cycling: Sprints', 'Rowing', 'Weight-Lifting', 'Track and Field: Weights']

    power_beg = ['Badminton', 'Auto Racing', 'Skateboarding', 'Track and Field: Distance', 'Rodeo: Bull/Bareback/Bronc Riding', 'Horse Racing', 'Cheerleading', 'Roller Skating', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    power_mid = ['Basketball', 'Gymnastics', 'Soccer', 'Skiing: Alpine', 'Water Polo', 'Rugby', 'Lacrosse', 'Field Hockey', 'Figure Skating', 'Cycling: Distance', 'Volleyball', 'Racquetball/Squash', 'Surfing', 'Fencing', 'Skiing: Freestyle', 'Team Handball', 'Bobsledding/Luge', 'Ski Jumping', 'Skiing: Nordic', 'Track and Field: High Jump', 'Diving', 'Swimming (all strokes): Distance', 'Rodeo: Calf Roping', 'Track and Field: Middle Distance', 'Swimming (all strokes): Sprints', 'Water Skiing', 'Table Tennis', 'Canoe/Kayak', 'Golf']
    power_pro = ['Boxing', 'Ice Hockey', 'Football', 'Wrestling', 'Martial Arts', 'Tennis', 'Baseball/Softball', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Speed Skating', 'Cycling: Sprints', 'Track and Field: Long, Triple jumps', 'Track and Field: Sprints', 'Rowing', 'Weight-Lifting', 'Track and Field: Weights']

    speed_beg = ['Auto Racing', 'Diving', 'Rodeo: Bull/Bareback/Bronc Riding', 'Weight-Lifting', 'Water Skiing', 'Track and Field: Weights', 'Horse Racing', 'Golf', 'Cheerleading', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    speed_mid = ['Boxing', 'Wrestling', 'Martial Arts', 'Gymnastics', 'Water Polo', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Field Hockey', 'Figure Skating', 'Cycling: Distance', 'Volleyball', 'Racquetball/Squash', 'Surfing', 'Fencing', 'Skiing: Freestyle', 'Team Handball', 'Ski Jumping', 'Badminton', 'Skiing: Nordic', 'Track and Field: High Jump', 'Swimming (all strokes): Distance', 'Skateboarding', 'Rowing', 'Rodeo: Calf Roping', 'Track and Field: Distance', 'Table Tennis', 'Canoe/Kayak', 'Roller Skating']
    speed_pro = ['Ice Hockey', 'Football', 'Basketball', 'Tennis', 'Baseball/Softball', 'Soccer', 'Skiing: Alpine', 'Lacrosse', 'Speed Skating', 'Cycling: Sprints', 'Bobsledding/Luge', 'Track and Field: Long, Triple jumps', 'Track and Field: Sprints', 'Track and Field: Middle Distance', 'Swimming (all strokes): Sprints']

    agility_beg = ['Auto Racing', 'Rowing', 'Track and Field: Distance', 'Weight-Lifting', 'Track and Field: Weights', 'Canoe/Kayak', 'Horse Racing', 'Golf', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    agility_mid = ['Boxing', 'Football', 'Wrestling', 'Martial Arts', 'Gymnastics', 'Skiing: Alpine', 'Water Polo', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Field Hockey', 'Speed Skating', 'Cycling: Distance', 'Fencing', 'Team Handball', 'Cycling: Sprints', 'Bobsledding/Luge', 'Ski Jumping', 'Skiing: Nordic', 'Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Diving', 'Swimming (all strokes): Distance', 'Skateboarding', 'Track and Field: Sprints', 'Rodeo: Calf Roping', 'Rodeo: Bull/Bareback/Bronc Riding', 'Track and Field: Middle Distance', 'Swimming (all strokes): Sprints', 'Water Skiing', 'Table Tennis', 'Cheerleading', 'Roller Skating']
    agility_pro = ['Ice Hockey', 'Basketball', 'Tennis', 'Baseball/Softball', 'Soccer', 'Lacrosse', 'Figure Skating', 'Volleyball', 'Racquetball/Squash', 'Surfing', 'Skiing: Freestyle', 'Badminton']

    flexibility_beg = ['Cycling: Distance', 'Cycling: Sprints', 'Bobsledding/Luge', 'Auto Racing', 'Weight-Lifting', 'Track and Field: Weights', 'Horse Racing', 'Roller Skating', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    flexibility_mid = ['Boxing', 'Ice Hockey', 'Football', 'Baseball/Softball', 'Soccer', 'Water Polo', 'Rugby', 'Lacrosse', 'Rodeo: Steer Wrestling', 'Field Hockey', 'Speed Skating', 'Volleyball', 'Team Handball', 'Ski Jumping', 'Badminton', 'Skiing: Nordic', 'Skateboarding', 'Track and Field: Sprints', 'Rowing', 'Rodeo: Calf Roping', 'Track and Field: Distance', 'Rodeo: Bull/Bareback/Bronc Riding', 'Track and Field: Middle Distance', 'Water Skiing', 'Table Tennis', 'Canoe/Kayak', 'Golf']
    flexibility_pro = ['Basketball', 'Wrestling', 'Martial Arts', 'Tennis', 'Gymnastics', 'Skiing: Alpine', 'Track and Field: Pole Vault', 'Figure Skating', 'Racquetball/Squash', 'Surfing', 'Fencing', 'Skiing: Freestyle', 'Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Diving', 'Swimming (all strokes): Distance', 'Swimming (all strokes): Sprints', 'Cheerleading']

    nerve_beg = ['Racquetball/Squash', 'Badminton', 'Track and Field: Sprints', 'Rowing', 'Track and Field: Distance', 'Track and Field: Middle Distance', 'Swimming (all strokes): Sprints', 'Table Tennis', 'Track and Field: Weights', 'Golf', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    nerve_mid = ['Ice Hockey', 'Basketball', 'Wrestling', 'Tennis', 'Baseball/Softball', 'Soccer', 'Water Polo', 'Lacrosse', 'Field Hockey', 'Speed Skating', 'Figure Skating', 'Cycling: Distance', 'Volleyball', 'Fencing', 'Team Handball', 'Cycling: Sprints', 'Skiing: Nordic', 'Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Swimming (all strokes): Distance', 'Rodeo: Calf Roping', 'Weight-Lifting', 'Water Skiing', 'Canoe/Kayak', 'Cheerleading', 'Roller Skating', 'Equestrian', 'Archery']
    nerve_pro = ['Boxing', 'Football', 'Martial Arts', 'Gymnastics', 'Skiing: Alpine', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Surfing', 'Skiing: Freestyle', 'Bobsledding/Luge', 'Ski Jumping', 'Auto Racing', 'Diving', 'Skateboarding', 'Rodeo: Bull/Bareback/Bronc Riding', 'Horse Racing']

    durability_beg = ['Racquetball/Squash', 'Badminton', 'Track and Field: Long, Triple jumps', 'Swimming (all strokes): Sprints', 'Table Tennis', 'Canoe/Kayak', 'Golf', 'Cheerleading', 'Roller Skating', 'Equestrian', 'Archery', 'Curling', 'Bowling', 'Shooting', 'Billiards', 'Fishing']
    durability_mid = ['Tennis', 'Baseball/Softball', 'Track and Field: Pole Vault', 'Field Hockey', 'Speed Skating', 'Figure Skating', 'Volleyball', 'Surfing', 'Fencing', 'Skiing: Freestyle', 'Team Handball', 'Cycling: Sprints', 'Bobsledding/Luge', 'Ski Jumping', 'Skiing: Nordic', 'Auto Racing', 'Track and Field: High Jump', 'Diving', 'Swimming (all strokes): Distance', 'Skateboarding', 'Track and Field: Sprints', 'Rowing', 'Rodeo: Calf Roping', 'Track and Field: Distance', 'Track and Field: Middle Distance', 'Weight-Lifting', 'Water Skiing', 'Track and Field: Weights', 'Horse Racing']
    durability_pro = ['Boxing', 'Ice Hockey', 'Football', 'Basketball', 'Wrestling', 'Martial Arts', 'Gymnastics', 'Soccer', 'Skiing: Alpine', 'Water Polo', 'Rugby', 'Lacrosse', 'Rodeo: Steer Wrestling', 'Cycling: Distance', 'Rodeo: Bull/Bareback/Bronc Riding']

    handeyecoordination_beg = ['Speed Skating', 'Figure Skating', 'Cycling: Distance', 'Diving', 'Swimming (all strokes): Distance', 'Track and Field: Sprints', 'Rowing', 'Track and Field: Distance', 'Track and Field: Middle Distance', 'Weight-Lifting', 'Swimming (all strokes): Sprints', 'Canoe/Kayak', 'Cheerleading', 'Roller Skating', 'Equestrian', 'Fishing']
    handeyecoordination_mid = ['Football', 'Wrestling', 'Gymnastics', 'Skiing: Alpine', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Surfing', 'Skiing: Freestyle', 'Cycling: Sprints', 'Bobsledding/Luge', 'Ski Jumping', 'Skiing: Nordic', 'Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Skateboarding', 'Rodeo: Bull/Bareback/Bronc Riding', 'Water Skiing', 'Track and Field: Weights', 'Horse Racing', 'Curling', 'Bowling', 'Billiards']
    handeyecoordination_pro = ['Boxing', 'Ice Hockey', 'Basketball', 'Martial Arts', 'Tennis', 'Baseball/Softball', 'Soccer', 'Water Polo', 'Lacrosse', 'Field Hockey', 'Volleyball', 'Racquetball/Squash', 'Fencing', 'Team Handball', 'Badminton', 'Auto Racing', 'Rodeo: Calf Roping', 'Table Tennis', 'Golf', 'Archery', 'Shooting']

    analyticalaptitude_beg = ['Track and Field: High Jump', 'Track and Field: Long, Triple jumps', 'Diving', 'Swimming (all strokes): Distance', 'Skateboarding', 'Track and Field: Sprints', 'Rodeo: Bull/Bareback/Bronc Riding', 'Weight-Lifting', 'Swimming (all strokes): Sprints', 'Water Skiing', 'Track and Field: Weights', 'Cheerleading', 'Roller Skating', 'Archery', 'Fishing']
    analyticalaptitude_mid = ['Boxing', 'Gymnastics', 'Skiing: Alpine', 'Water Polo', 'Rugby', 'Rodeo: Steer Wrestling', 'Track and Field: Pole Vault', 'Speed Skating', 'Figure Skating', 'Cycling: Distance', 'Volleyball', 'Surfing', 'Skiing: Freestyle', 'Team Handball', 'Cycling: Sprints', 'Bobsledding/Luge', 'Ski Jumping', 'Badminton', 'Skiing: Nordic', 'Rowing', 'Rodeo: Calf Roping', 'Track and Field: Distance', 'Track and Field: Middle Distance', 'Table Tennis', 'Canoe/Kayak', 'Equestrian', 'Curling', 'Bowling', 'Shooting', 'Billiards']
    analyticalaptitude_pro = ['Ice Hockey', 'Football', 'Basketball', 'Wrestling', 'Martial Arts', 'Tennis', 'Baseball/Softball', 'Soccer', 'Lacrosse', 'Field Hockey', 'Racquetball/Squash', 'Fencing', 'Auto Racing', 'Horse Racing', 'Golf']

    group_skills = endurance_beg,endurance_mid,endurance_pro
    print(group_skills)

    def waarde_bepalen(z):
        total_list_user = []
        skill_lijst_lp = ["endurance", "strength", "power", "speed", "agility", "flexibility", "nerve", "durability", "handeyecoordination", "analyticalaptitude"]
        for x in z:
            for skill in skill_lijst_lp:
                skill_list = skill + "_" + x
                print(skill_list)
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

@app.route("/home")
def home():
    return 'home.html'


@app.route("/quiz/<qid>")
def quiz(qid):
    
    questions_string = {
        "1": "endurance;Your friends asks you if you\'d like to sign up for a charity run with them. What do you say?;\
            You\'ll cheer them on from the sidelines.;If it\'s no more than 5 km, you\'ll consider it.;Absolutely!",
        "2": "strength;You are helping your friends with moving to their new appartment. What kind of stuff would you prefer to carry?;\
            The plants and other light stuff;The heavier moving Boxes;Carrying the couches and fridge",
        "3": "power;You are at a theme park where you can win prizes by shooting or throwing the ball really hard. How many prices could you win?;\
            Participating is more important than winning;Winning the small prices;Getting all the big prices",
        "4": "speed;If you would descripe your speed in the form of animals, which animal would you been?;\
            A Tortoise;A rabbit;A cheetah",
        "5": "agility;If we refer to the movement of your body, how would you describe it?;\
            I don't move easily and I am not quick;I move easily but I am not really quick;I move easy and quick",
        "6": "flexibility;If you were to take a yoga class, what would it look like?;\
            Nope;Doing alright;Master",
        "7": "nerve;How do you feel about adrenaline sports?;\
            Nope nope nope;Rollercoasters are fine but skydiving is a bit much;Skydiving is my biggest dream",
        "8": "durability;How do you feel about adrenaline sports?;\
            Nope nope nope;Rollercoasters are fine but skydiving is a bit much;Skydiving is my biggest dream",
        "9": "hand-eye coordination;When someone throws you a ball, you are confident you'll catch it.;\
            Nervous, you're not usually good at catching things;Focused, you'll probably catch it if you pay attention;Yes!",
        "10": "analytical aptitude;Are you comfortable with making fast important decissions under pressure for yourself or a group?;\
            I am bad at making fast descissions under pressure;I am oke with it if it's at least for my own businesses;I can take the pressure and do what is the best for myself and the group"
    }

    data = questions_string[qid]
    return str(data)