import csv

df = []

with open("main.csv", "r") as f:
    reader = csv.reader(f)

    for i in reader:
        df.append(i)

header = df[0]
planet_data = df[1:]

header[0] = 'row_num'


planetData = list(planet_data)

for i in planetData:
    planet_mass = i[3]

    if planet_mass.lower() == 'unknown':
        planet_data.remove(i)
        continue
    
    else:
        massValue = planet_mass.split(" ")[0]
        massRef = planet_mass.split(" ")[1]

        if massRef == 'Jupiters':
            massValue = float(massValue) * 317.8
        
        i[3] = massValue

    planet_radius = i[7]

    if planet_radius.lower() == 'unknown':
        planet_data.remove(i)
        continue
    
    else:
        radiusValue = planet_radius.split(" ")[0]
        radiusRef = planet_radius.split(" ")[2]

        if radiusRef == 'Jupiter':
            radiusValue = float(radiusValue) * 11.2
        
        i[7] = radiusValue

massValue = []
radiusValue = []
planet_names = []

for i in planet_data:
    planet_names.append(i[1])
    massValue.append(i[3])
    radiusValue.append(i[7])

planetGravity = []
#header[19] = 'Gravity'

for index, name in enumerate(planet_names):
    gravity = (float(massValue[index])*5.972e+24) / (float(radiusValue[index])*float(radiusValue[index])*6371000*6371000) * 6.674e-11
    planetGravity.append(gravity)
    
    planet_data[index].append(gravity)

header.append('gravity')


#print(header)
#print(planet_data[1])