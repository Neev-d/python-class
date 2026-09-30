waypoints = [(0,0), (2, 3), (5, 1)]
for wp in waypoints:
    print("Heading to", wp)
#--------------------------------------

for i in range(3):
    print("scan", i)
print("---")

for i in range (1, 6):
    print(i, end = " " )
    
for i in range(10, 0, -2):
    print(i, end = " ")
print()
#--------------------------------------------
#accumulator pattern
readings = [22.5, 23.1, 21.8, 24.0, 22.9]
total = 0
for r in readings:
    total += r
print(f"sum :{total:.2f}")
print("count :", len(readings))
print(f"mean : {total/len(readings):.2f}")
#-------------------------------------------------
#NESTED LOOPS
obstacles = [(1,2), (3, 3), (0, 4)]
for row in range(5):
    for col in range(5):
        if(row, col) in obstacles:
            print("#", end="")
        else:
            print(".", end = "")
    print()
#-------------------------------------------------------
""""
    write a pyton program to generate a grid of 8x8 and place at least 3 obstacles at 
    positions of your choice, then add a start marker S at (0,0) and a goal G at (7,7).
"""

obstacles = [(2, 3), (1, 7), (5,5)]
for i in range(8):
    for j in range(8):
        if (i,j) in obstacles:
            print("X", end = " ")
        else:
            if (i,j) == (0, 0):
                print("S", end = " ")
            elif (i, j) == (7, 7):
                print("G")
            else:
                print(".", end = " ") 
    print()
#-------------------------------------------------------------------
readings = [12, -1, 34, 78, 15]
for r in readings:
    if r<0:
        continue
    if r>70:
        print("Danger at", r)
        break
    else:
        print("all readings safe")
