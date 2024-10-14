def main():
    #open file and read to the list
    with open('constitution2.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    while True:
        #promp for search
        search_term = input("enter a search term").strip()
        if not search_term:
            break

        #loop each line for search term
        for i, line in enumerate(lines):
            if search_term.lower() in line.lower():
                section_start = i
                while section_start > 0 and lines[section_start - 1] != '':
                    section_start -= 1

                #find the end of section
                section_end = i
                while section_end < len(lines) - 1 and lines[section_end + 1] != '':
                    section_end += 1

                #print the search term
                print(f"\nFound at line {i +1}:")
                for j in range(section_start, section_end + 1):
                    print(lines[j])

                    i = section_end