

# The questions for the quiz
# big, mid, pro value

# Endurance 
# Your friends asks you if you'd like to sign up for a charity run with them. What do you say?
# a) Absolutely!
# b) If it's no more than 5 km, you'll consider it.
# b) You'll cheer them on from the sidelines.

# Strength
# You are helping your friends with moving to their new appartment. What kind of stuff would you prefer to carry?
# a) The plants and other light stuff
# b) The heavier moving Boxes 
# c) Carrying the couches and fridge

# Power
# You are at a theme park where you can win prizes by shooting or throwing the ball really hard. How many prices could you win?
# a) participating is more important than winning
# b) Winning the small prices
# c) Getting all the big prices

# Speed
# If you would descripe your speed in the form of animals, which animal would you been?
# a) A Tortoise
# b) A rabbit
# c) A cheetah

# /Agility (5)
# If we refer to the movement of your body, how would you describe it?
# a) I don't move easily and I am not quick
# b) I move easily but I am not really quick
# c) I move easy and quick

# Flexibility
# If you were to take a yoga class, what would it look like?
# a) Master
# b) Doing alright
# c) Nope

# Nerve
# How do you feel about adrenaline sports?
# a) Skydiving is my biggest dream
# b) Rollercoasters are fine but skydiving is a bit much
# c) Nope nope nope

# Durability
# You are at a concert and see people doing the slamdance. Are you joining the moshpit?
# a) I am staying as far as possible
# b) I join it a bit on the edge
# c) I would like to join in the center

# Hand-eye coordination
# When someone throws you a ball, you are
# a) confident you'll catch it
# b) focused, you'll probably catch it if you pay attention
# c) nervous, you're not usually good at catching things

# Analytical aptitude
# Are you comfortable with making fast important decissions under pressure for yourself or a group?
# a) I bad at making# fast descissions under pressure
# b) I am oke with it if it's at least for my own businesses 
# c) I can take the pressure and do what is the best for myself and the group



"""
# /intense
# beter of niet (niet -> reverse list)

# b is wat je bent maar je zou c kunnen bereiken. b ontwikkelen leidt tot c.

# It is heavily raining outside and you need to run from your car towards your frontdoor. How would you end up after this 50 meters?
# a) I would end up changing my clothes
# b) My jacket and jeans needs to dry for a short period of time
# c) Only need to dry my hair a bit

# You are playing a game of football(socces). You have the ball and need to pass it. What would your best play be? 
# a) The safest way is to pass it back to the goalkeeper
# b) I play it to the nearest player.
# c) I give the perfect assist.
# beseffen van wat er om je heen gebeurt
"""



# The output for the generated sport

# Saving the skills based on predefined values
# Skill in 3 levels (beg,mid,pro)
# endurance_beg = []
# endurance_mid = []
# endurance_pro = []

# Get row from specific ID
# SELECT * FROM users WHERE ID = (value from localstorage)
# Put the row in a varaible to use later on
# skill_values_user = {id:3, name:"test", age:30, flexibility:mid, power:pro}

# Every value in a column creats a list with the sport that belongs to it
# Skill_values_user = {id:3, name:"test", age:30, flexibility:mid, power:pro}

# list to loop through for only the skills
# skill_lijst = ["endurance", "strength", "power", "speed", "agility", "flexibility", "nerve", "durability", "handeyecoordination", "analyticalaptitude"]
# empty list to fill all the sports with to compare later on
# total_list_user = []

# # function to put skill lijst in go through
# def waarde_bepalen(z):
#     #getting x and y from the dict   
#     for x, y in z.items():
#         #looping through skill list
#         for w in skill_lijst:
#             #If in skilllist put key and value together and get the function with the same name as string.
#             if x == w:
#                 search_list = x + "_" + y
#                 #put predifined list into list of user
#                 total_list_user.append(globals()[search_list])        
#             else:
#                 pass
#    # get lists out of list and return one complete list
#    return total_list_user = [item for sublist in test_lijst for item in sublist]

# Loop through the list to choose for one sport
# from collections import Counter
# total_list_user = [...]
# Counter(total_list_user)
# Counter({'football': 6, 'boxing': 4, 'fishing': 1})
# next(iter(counter)) or total_list_user((i, a.count(i)) for i in a)
