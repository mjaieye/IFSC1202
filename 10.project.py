class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score != '' else None for score in scores]

    def RunningAverage(self):
        # Calculate the running average, excluding None (missing scores)
        non_blank_scores = [score for score in self.Grades if score is not None]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        return 0.0

    def TotalAverage(self):
        # Calculate the total average, treating None (missing scores) as zero
        total_scores = [score if score is not None else 0 for score in self.Grades]
        if total_scores:
            return sum(total_scores) / len(total_scores)
        return 0.0

    def LetterGrade(self):
        # Determine the letter grade based on the TotalAverage
        avg = self.TotalAverage()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

# Function to read the file and create Student objects
def process_students(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line by commas and remove any leading/trailing whitespace
            data = line.strip().split(',')
            firstname = data[0].strip()
            lastname = data[1].strip()
            tnumber = data[2].strip()
            scores = data[3:]  # The rest of the list are scores
            # Create a Student object and add it to the list
            students.append(Student(firstname, lastname, tnumber, scores))
    return students

# print the report
def print_report(students):
    # Print the header
    print(f"{'First Name':>10}   {'Last Name':>10} {'ID':>10} {'Running Average':>12} {'Semester Average':>12} {'Letter Grade':>12}")
    print("-" * 66)
    # Print each student's information
    for student in students:
        print(f"{student.FirstName:>10} {student.LastName:>10} {student.TNumber:>10} "
              f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

#program logic
if __name__ == "__main__":
    # Load the student data from the file and create student objects
    students = process_students('10.project student score.txt')
    # Print the report
    print_report(students)
