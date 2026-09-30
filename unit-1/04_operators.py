heading = 359
turn = 5
print("Wrong:", heading + turn)
print("right:", (heading + turn)%360)
print("negative:", (-30)%360)
#-------------------------------------------------------
distance = 8.0
limit = 10
print(distance < limit)
print(distance == limit)
print(0 <= distance < limit)
battery = 45
print(distance>5 and battery > 20)
print(distance>5 or battery > 90)
print(distance>5)
#--------------------------------------------------------------------------2q
"""
    WRITE A PYTHON PROGRAM WITH SINGLE EXPRESSION THAT IS TRUE ONLY WHEN THE ROBOT IS
    SAFE TO MOVE: DISTANCE > 10, BATTERY > 20, NOT CURRENTLY DOCKED"""

distance = 35
battery = 50
docked = True
print(distance>10 and battery>20 and docked)