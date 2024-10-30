#define the class ocject
class student():
    def __init__(self, firstname, lastname, tnumber, score):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grade = [float(score) if score != '' else none score in score]

