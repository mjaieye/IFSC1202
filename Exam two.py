import csv

properties = []

try:
    with open('exam two properties.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            row[4] = float(row[4])

            properties.append(row)
except FileNotFoundError:
    print("Error: File 'exam two properties.csv' not found.")
    exit()

zipcodes = []

for property in properties:
    property_zip = property[3]  
    property_price = property[4]  

    
    found = False
    for zipcode in zipcodes:
        if zipcode[0] == property_zip:
        
            zipcode[1] += 1
            zipcode[2] += property_price
            found = True
            break
    
    if not found:
        zipcodes.append([property_zip, 1, property_price])

print("\nZIPCODE     COUNT      AVERAGE")
for zipcode in zipcodes:
    zip_code = zipcode[0]
    count_of_properties = zipcode[1]
    avg_price = zipcode[2] / count_of_properties if count_of_properties != 0 else 0
  
    print(f"{zip_code:>8}  {count_of_properties:>5}    ${avg_price:,.2f}")
