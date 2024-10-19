import csv

#read csv file
filename = '09.Prpject Distances.cvs'
with open(filename, mode='r') as file:
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