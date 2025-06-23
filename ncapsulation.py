class Student:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def display_info(self):
        print(f"Student: {self.name},Email:{self.email}")
    def upadate_email(self,new_email):
        self.email=new_email
        print(f"Email updated to {self.email}")

class Course:
    def __int__(self,title,duration):
        self.title=title
        self.duration=duration # in weeks
    def show_details(self):
        print(f"Course:{self.title}, Duration:{self.duration} weeks")
    def change_duration(self,new_duration):
        self.duration=new_duration
        print(f"Duration updated to {self.duration} Weeks")

class Trainer:
    def __int__(self,name,expertise):
        self.name=name
        self.expertise=expertise
    def assign_course(self,course):
        print(f"{self.name}is assigned to {course.title}")
    def introduction(self):
        print(f"I am {self.name},expert in {self.expertise}")
class Enrollment:
    def __int__(self,student,course):
        self.student=student
        self.course=course
    def confirm_enrollment(self):
        print(f"{self.student.name} enrolled in{self.course.titlle}")
    def confirm_enrollment(self):
        print(f"{self.student.name}'s enrollment in {self.course.title} is canceled")

s1=Student("Sharan","shawaldar@evolent.com")
#c1=Course("Python",8)
t1=Trainer("Alice","Data Science")

c1 = Course("Python",8)
c1.show_details()
c1.change_duration(10)

s1.display_info()
s1.upadate_email("bhsharan.sharan03@gmail.com")

'''c1.show_details()
c1.change_duration(10)'''

t1.introduction()
t1.assign_course(c1)

enroll=Enrollment(s1,c1)
enroll.confirm_enrollment()
enroll.cancel_enrollment()



