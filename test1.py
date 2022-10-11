Skill_values_user = {"flexibility":"2", "speed":"3", "agility":"1"}

skill_lijst = ["endurance", "strength", "power", "speed", "agility", "flexibility", "nerve", "durability", "handeyecoordination", "analyticalaptitude"]

speed3 = ["test3"]
flexibility2 = ["test1"]
agility1 = ["test2", "test10"]
test_lijst = []


for x, y in Skill_values_user.items():
    for w in skill_lijst:
        if x == w:
            search_list = x + y
            test_lijst.append(globals()[search_list])        
        else:
            pass

test_lijst = [item for sublist in test_lijst for item in sublist]

print(test_lijst)
