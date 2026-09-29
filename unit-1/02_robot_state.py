robot_name = "Alpha"
battery_pct = 78.5
is_docked = True
waypoints = 12
print("---")
print(type(robot_name))
#----------------------------------------------

battery = 100
print("start: ", battery)
battery = battery - 15
print("after: ", battery)
battery -= 15
print("later: ", battery)
#-------------------------------------------------------------

#INDENTATION:
battery = 45
if battery < 50:
    print("Charging recommended")
    print("Docking now...")
print("Status check done")
#----------------------------------------------------------------

""""
    WRITE A PYTHON PROGRAM WITH A FILE NAME ROBOT_STATE.PY WITH 4 VARIABLES 
    DESCRIBING A ROBOT OF YOUR CHOICE PRINT THEM & THE ADD AN IF BLOCK THAT PRINTS A 
    WARNING WHEN THE BATTERY IS BELOW 50"""

robot_name = "Beta"
Battery_pct = 45
docked = False
points = 17
print(robot_name, battery_pct, docked, points)

if battery < 50:
    print("BATTERY IS LOW")

