import numpy as np
import matplotlib.pyplot as plt

# Assumptions:
# Rooms are square
# Thermal resitance of the roof is the same as the walls

# Mode:
# Either F or C Display
displayinC = False

initial_house_temp = 25.5556
r = 10
U = 1 / r
house_outside_heat_capacity = .0229 * 1000 # W/Degrees C
house_inside_heat_capacity = .016854 * 1000 # W/Degrees C
house_floor_area = 88 # Square meters
house_external_perimeter = 9.32 * 4 # Meters
house_height = 3.2 # Meters
wall_thickness = 0.05 # Meters
wall_volume = wall_thickness * house_height * house_external_perimeter # Cubic meters
C = house_inside_heat_capacity * house_floor_area * house_height + house_outside_heat_capacity * wall_volume # W/Degrees C
timestep = 60 # Minutes
tempsfile = open("hourlytempsduringheatwave", "r")
temps = []
for line in tempsfile:
    for num_str in line.split():
        temps.append(float(num_str))
insidetemps = []
outsidetemps = []

housetemp = initial_house_temp

def house_temperature_model(prev_insidetemp, prev_outsidetemp, timestep):
    u_diff_temp = U*(prev_insidetemp - prev_outsidetemp)
    deltatoverC = timestep * 60 / C
    calculatedtempchange = deltatoverC * - u_diff_temp
    newtemp = prev_insidetemp + calculatedtempchange
    return newtemp

i = 0
for i in range(len(temps)):
    housetemp = house_temperature_model(housetemp, temps[i], timestep)
    if not displayinC:
        disphousetemp = housetemp * 9 / 5 + 32
        dispoutsidetemp = temps[i] * 9 / 5 + 32
    else:
       dispoutsidetemp = temps[i]
    dispoutsidetemp = round(dispoutsidetemp, 4)
    disphousetemp = round(disphousetemp, 4)
    print("Time: " + str(i))
    print("Outside Temp: " + str(dispoutsidetemp))
    print("Inside Temp: " + str(disphousetemp))
    print("")
    outsidetemps.append(dispoutsidetemp)
    insidetemps.append(disphousetemp)