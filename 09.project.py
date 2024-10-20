import csv

#read csv file
filename = '09.Prpject Distances.cvs'
with open(filename, mode = 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

#display the 2D list
for row in data:
    print(' '.join(f'{item:>10}'for item in row))

#promp for user input
from_city = input("entry from city: ").strip()
to_city = input("enter to city: ").strip()

#search the city in the table
from_city_index = -1
to_city_index = -1

#find the index from city
for i, row in enumerate(data):
    if row[0]. lower() == from_city.lower():
        from_city_index = i
        break

#frind the index to city
if data:
    for j, city in enumerate(data[0]):
        to_city_index = j
        break

#check for invalid city
if from_city_index == -1:
    print("invalid from city")
elif to_city_index == -1:
    print("invalid to city")
else:
    diatance = data[from_city_index][to_city_index]
    print(f"{from_city} ot {to_city} - {diatance} miles")