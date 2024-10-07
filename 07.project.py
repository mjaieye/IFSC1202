#function to parse the string (DD MM SS)
def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)
    minute_symbol = "'"
    second_symbol = '"'

    #extract (DD MM SS)
    degrees = float(ddmmss.split(degree_symbol)[0])
    minutes = float(ddmmss.split(degree_symbol)[1].split(minute_symbol)[0])
    second = float(ddmmss.split(degree_symbol)[1].split(second_symbol)[0])

    return degrees, minutes, seconds

#function to convert DMS to decimal degree
def DDMMSStoDecimal(degrees, minutes, seconds):
    #to decimal degree
    decimal_degrees = degrees + (minutes/60) + (seconds/3600)
    return decimal_degrees

#file read and write function
def precess_angle_file(input_file, output_file):
    with open(input_file,'r')as file:
        lines = file.readline()

    processed_values = []
    for line in lines:
        #strip extra whitespace
        ddmmss = line.strip()

        #

    