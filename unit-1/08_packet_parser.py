raw = "Alpha Rover"
print(f"[{raw}]")
print(f"[{raw.strip()}]")
print(raw.strip().lower())
print(raw.strip().upper())
print(raw.strip().replace(" ", "_"))
print("Rover" in raw)
#----------------------------------------

packet = "T:25;H:60;B:78"
fields = packet.split(";")
print(fields)
key, value = 0, 0
for field in fields:
    key, value = field.split(":")
    print(key, "->", float(value))
print(key, value)
#-------------------------------------------------------------------------------------

"""
    write a program inventing your own packet format, gps coordinates, motor currents, 
    whatever you like. and parse it into labelled values
"""

details = "gps_coordinates:12, 45, 80; motor currents:0.5"
details = details.split(";")
for i in details:
    key, value = i.split(":")
    print(details)
    print(key, "->", int(value))