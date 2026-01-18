class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def display(self):
        print(f"Student name: {self.name} with roll no.: {self.roll_no}")

s1 = Student("Mohit", 19)
s2 = Student("Rohit", 20)
s1.display()
s2.display()


