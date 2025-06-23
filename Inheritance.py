class School:
    name ="VVSW"
    def attaandance(self):
        print("attandance")

class Student(School):
    def printStudent(self):
        print("This is inside the student")

class Teacher(School):
    def printTeacher(self):
        print("This is inside the school")

class Staff(School):
    def printStaff(self):
        print("This is inside the staff")

print("The Student Details")
s =Student()
s.printStudent()
s.attaandance()
print(s.name)
print("-------------------/nThe staff details")
staff = Staff()
staff.printStaff()
staff.attaandance()
print(staff.name)

