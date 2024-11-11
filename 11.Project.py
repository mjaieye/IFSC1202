# 11.Project.py

class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        non_blank_scores = [float(grade) for grade in self.Grades if grade != ""]
        if non_blank_scores:
            return sum(non_blank_scores) / len(non_blank_scores)
        return 0.0

    def TotalAverage(self):
        total_scores = [float(grade) if grade != "" else 0 for grade in self.Grades]
        return sum(total_scores) / len(total_scores) if total_scores else 0.0

    def LetterGrade(self):
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        for index, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return index
        return -1

    def print_student_list(self):
        header = "{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            "First Name", "Last Name", "ID Number", "Running Avg", "Semester Avg", "Grade"
        )
        print(header)
        print("-" * len(header))
        for student in self.Studentlist:
            print("{:<12} {:<12} {:<12} {:<12.2f} {:<12.2f} {:<12}".format(
                student.FirstName, student.LastName, student.TNumber,
                student.RunningAverage(), student.TotalAverage(), student.LetterGrade()
            ))

    def add_student_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(',')
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                tnumber, score = line.strip().split(',')
                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(score)


# Main Program
student_list = StudentList()
student_list.add_student_from_file("11.Project Students.txt")
student_list.add_scores_from_file("11.Project Scores.txt")
student_list.print_student_list()
