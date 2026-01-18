class Student:
    #class attributes
    school_name = "Open AI School"
    total_students = 0

    def __init__(self, name, marks):
        #instance attributes
        self.name = name
        self.marks = marks
        #accessing class attribute using class name
        Student.total_students += 1
    
    #instance method
    def display_info(self):
        print(f"Student name: {self.name}\nStudent marks: {self.marks}\nSchool name: {Student.school_name}\n")
    
    #classmethod
    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students
    
    #staticmethod
    @staticmethod
    def is_pass(marks):
        return marks >= 40
    
    # ----------- USING THE CLASS -------------

s1 = Student("Mohit", 99)
s2 = Student("Riya", 34)

s1.display_info()
s2.display_info()

print("Total students in school", Student.get_total_students())

#change school for all students
Student.change_school("Ai cultured school.")

s1.display_info()
s2.display_info()

#using staticmethod
print("Is Mohit passed -> ", Student.is_pass(s1.marks))
print("Is Riya passed ->", Student.is_pass(s2.marks))