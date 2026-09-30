temp = 45.0
if temp > 40:
    print("Cooling on")
print("Check complete")
#----------------------------------------------------
temp = float(input("Enclosure temperature: "))
if temp < 40:
    mode = "heater on"
elif temp <= 40:
    mode = "normal"
elif temp <= 60:
    mode = "cooling"
else:
    print("Shut down")
print("Operating mode:", mode)
#--------------------------------------------------------------1
marks = 95
if marks >= 40:
    grade = "PASS"
elif marks >= 90:
    grade = "DISTINCTION"
else:
    grade = "FAIL"
print(grade)


