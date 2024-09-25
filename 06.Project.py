# Open input and output files
with open('06.project input File.txt', 'r') as input_file, open('06.Project Output File.txt', 'w') as output_file:
    #input file
    for line in input_file:
        if '**insert merge file here**' in line:
            # If the merge point is found, open the merge file and write its content to the output file
            with open('06.project merge file.txt', 'r') as merge_file:
                for merge_line in merge_file:
                    output_file.write(merge_line)
        else:
            # input to output file
            output_file.write(line)
    
    #success message
    print("Files have been successfully merged.")
