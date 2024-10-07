# Function to parse the string in DMS
def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)
    minute_symbol = "'"
    second_symbol = '"'

    # Extract DMS
    degrees = float(ddmmss.split(degree_symbol)[0])
    minutes = float(ddmmss.split(degree_symbol)[1].split(minute_symbol)[0])
    seconds = float(ddmmss.split(minute_symbol)[1].split(second_symbol)[0])
    
    return degrees, minutes, seconds

# Function to convert DMS into decimal degrees
def DDMMSStoDecimal(degrees, minutes, seconds):
    #to decimal degrees
    decimal_degrees = degrees + (minutes / 60) + (seconds / 3600)
    return decimal_degrees

# File read, write functions
def process_angle_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    processed_values = []
    
    for line in lines:
        # Strip any extra whitespace
        ddmmss = line.strip()
        
        # Parse the DMS
        degrees, minutes, seconds = ParseDegreeString(ddmmss)
        
        #to decimal degrees
        decimal_value = DDMMSStoDecimal(degrees, minutes, seconds)
        
        #processed value to the list
        processed_values.append(decimal_value)
    
    #processed values to the output file
    with open(output_file, 'w') as file:
        for value in processed_values:
            file.write(f"{value}\n")
    
    return len(processed_values)  # Return the number of records processed

# file usage
input_filename = '07.Project Angles Input.txt'
output_filename = '07.Project Angles Output.txt'

# Process the file
records_processed = process_angle_file(input_filename, output_filename)
print(f"{records_processed} records processed")
