#define the class ocject
class student():
    def __init__(self, firstname, lastname, tnumber, score):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grade = [float(score) if score != '' else none score in score]

    def RynningAverage(self):
        non_blank_scores = [score for score in self.Grades if score is not None]
        if not non_blank_scores:
            return 0
        return sum(non_blank_scores / len(non_blank_scores)

    def totalAverage(self):
        total_score = [score if score is not None else 0 for score in self.Grades]
        if not total_score:
            return 0
        return sum(total_scores) / len(total_scores)

    def lettergrade(self):
        avg = self.totalAverage()
        if avg >=90:
            return "a"
        elif avg >=80:
            return "b"
        elif avg >= 70:
            return "c"
        elif avg >= 60:
            return "d"
        else
            return "f"

def reda_student_data(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            data = line. strip(). split(',')
            firstname, lastname, tnumber = data[0], data[1], data[2]
            score = data[3:]
            students.append(student(firstname, lastname, tnumber, scores))
    return students

def display_student_info(students):
    print(f"{'first name':<12} {'last name'<12} {'id':<10} {'running average':<15} {'semester average':<15} {'letter grade':<10}")
    print("-" * 70)
    for student in students:
        running_avg = student.runningAverage()
        total_avg = student.totalAverage()
        letter_grade = student.lettergrade()
        print(f"{student.firstname:<12} {student.lastname:<12} {student.tnumber:<:10} {running_avg:<15.2f} {letter_grade:<10}")

students = read_student_data("10.project student score.txt")
display_student_info(students)