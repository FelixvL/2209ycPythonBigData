import pandas as pd

# dit moet in app.py uiteindelijk

questions = {
    '1': {'skill': 'endurance',
          'question': 'Your friends asks you if you\'d like to sign up for a charity run with them. What do you say?',
          'a': 'Absolutely!', 
          'b': 'If it\'s no more than 5 km, you\'ll consider it.',
          'c': 'You\'ll cheer them on from the sidelines.'},
    '2': {'skill': 'flexibility',
          'question': 'If you were to take a yoga class, what would it look like?',
          'a': 'Master', 
          'b': 'Doing alright',
          'c': 'Nope'}
}

questions_string = {
    1: "endurance;Your friends asks you if you\'d like to sign up for a charity run with them. What do you say?;\
        Absolutely!;If it\'s no more than 5 km, you\'ll consider it.;You\'ll cheer them on from the sidelines."
}

print(questions.endurance.question)
print(questions.endurance.a)


@app.route("quiz/<id>")
def quiz(id):
    return questions_string[id]


# def interpret_results():

#     # is half pseudocode om idee uit te werken, runt niet.
#     newlist = []
#     if user.endurance >= 6.5:
#         newlist.append(sports[sports.endurance >= 6.5])
#     elif user.endurance >= 4:
#         newlist.append(sports[sports.endurance >= 4])
#     else:
#         newlist.append(sports[sports.endurance < 4])

    #calculate frequency van newlist

# Endurance 
# Your friends asks you if you'd like to sign up for a charity run with them. What do you say?
# a) Absolutely! (6,5+)
# b) If it's no more than 5 km, you'll consider it. (4-6,5)
# c) You'll cheer them on from the sidelines. (4-)

# Strength 

# Power 
# Throw a ball really hard or jump far/high

# Speed
# Reactievermogen 

# Agility (5)
# Quick feet
# Dance tiles arcade

# Flexibility
# If you were to take a yoga class, what would it look like?
# a) Master (7+)
# b) Doing alright (4-7)
# c) Nope (4-)

# Nerve
# How do you feel about adenaline sports?
# a) Skydiving is my biggest dream (8+)
# b) Rollercoasters are fine but skydiving is a bit much (4-8)
# c) Nope nope nope (4-)

# Durability
# Kun je tegen een stootje?

# Hand-eye coordination
# When someone throws you a ball, you are
# a) confident you'll catch it (6+)
# b) focused, you'll probably catch it if you pay attention (6-)
# c) nervous, you're not usually good at catching things

# Analytical aptitude
# Do you like to think about tactics? (puzzles, chess etc)
# a) 
# a) Yes, I love figuring out the best strategy (6+)
# b) No, I don't want to think too much during my workout (6-)

# intense
# beter of niet (niet -> reverse list)

