class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor called.")
    
    def introduction(self):
        print(f"Hello, I'm {self.name}")
    
    def role(self):
        print("Role: Person")

class Student(Person):
    def __init__(self, name, roll_no):
        #parent constructor called.
        super().__init__(name)
        self.roll_no = roll_no
        print("Student constructor called.")
    
    def role(self):
        print("Role: Student.")

class Athlete:
    def role(self):
        print("Role: Athlete")

#Multiple inheritance
class StudentAthlete(Student, Athlete):
    def __init__(self, name, roll_no, sport):
        super().__init__(name, roll_no)
        self.sport = sport
        print("Student-Athlete constructor called.")

    def display_info(self):
        print(f"Student Name: {self.name}\nStudent Roll no.: {self.roll_no}\nSports: {self.sport}")

# ----------- USING THE CLASSES -------------

s1 = StudentAthlete("Mohit", 19, "Cricekt")

s1.introduction()
s1.role()
s1.display_info()

#MRO
print("\nMRO order.")
print(StudentAthlete.__mro__)