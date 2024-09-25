# File paths
input_file_path = "06.Project Input File.txt"
merge_file_path = "06.Project Merge File.txt"
output_file_path = "06.Project Output File.txt"

# Initialize record counters
input_records = 0
merge_records = 0
output_records = 0

# Open files
with open(input_file_path, 'r') as input_file, open(merge_file_path, 'r') as merge_file, open(output_file_path, 'w') as output_file:
    # Read and process the input file
    for line in input_file:
        input_records += 1  # Increment input record count
        if '**Insert Merge File Here**' in line:
            # Write the part of the line before the placeholder to output
            output_file.write(line.split('**Insert Merge File Here**')[0])
            output_records += 1

            # Copy the contents of the merge file
            merge_file.seek(0)  # Move to the start of the merge file
            for merge_line in merge_file:
                output_file.write(merge_line)
                merge_records += 1  # Increment merge record count
                output_records += 1  # Increment output record count
            
            # Write the part of the line after the placeholder, if any
            if line.split('**Insert Merge File Here**')[1]:
                output_file.write(line.split('**Insert Merge File Here**')[1])
                output_records += 1

        else:
            output_file.write(line)
            output_records += 1  # Increment output record count

# Print the results
print(f"Input file records: {input_records}")
print(f"Merge file records: {merge_records}")
print(f"Output file records: {output_records}")
