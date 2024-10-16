import csv
import os

# Step 1: Check if the file exists in the current directory
filename = '09.Project Distances.csv'

# Debug: Check if the file exists
if not os.path.isfile(filename):
    print(f"Error: The file '{filename}' does not exist in the current directory.")
else:
    # Step 2: Read the CSV file and load the data into a 2D list
    data = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([item.strip() for item in row])  # Remove extra spaces from each item

    # Debug: Check if data was read properly
    if not data:
        print("Error: The file was read, but it is empty or improperly formatted.")
    else:
        # Display the 2D list as a formatted table
        # Print the header row (first row) with cities
        header_row = data[0]
        print(f"{'Cities':>10}", end='   ')
        for city in header_row[1:]:
            print(f"{city:>10}", end='   ')
        print()

        # Print each row with the city name followed by the distances
        for row in data[1:]:
            print(f"{row[0]:>10}", end='   ')
            for distance in row[1:]:
                print(f"{distance:>10}", end='   ')
            print()

        # Step 3: Prompt for user input
        from_city = input("Enter From City: ").strip()
        to_city = input("Enter To City: ").strip()

        # Step 4: Search for the From City and To City in the table
        from_city_index = -1
        to_city_index = -1

        # Find the index of the From City in the first column
        for i, row in enumerate(data):
            if row[0].lower() == from_city.lower():
                from_city_index = i
                break

        # Find the index of the To City in the first row
        for j, city in enumerate(data[0]):
            if city.lower() == to_city.lower():
                to_city_index = j
                break

        # Debugging: print indices to check if cities were found correctly
        print(f"From City Index: {from_city_index}, To City Index: {to_city_index}")

        # Step 5: Display the results based on the validity of the cities
        if from_city_index == -1:
            print("Invalid From City")
        elif to_city_index == -1:
            print("Invalid To City")
        else:
            distance = data[from_city_index][to_city_index]
            print(f"{from_city} to {to_city} - {distance} miles")
