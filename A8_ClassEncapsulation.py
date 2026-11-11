'''
Create a parent class called Human with:
    • attributes: first_name, family_name
    • a method __str__() that prints the full name
2.Create a child class called Student that inherits from Human.
The class should include:
    • a private attribute __student_id
    • two methods:
        • set_student_id(value) → set the student ID (must be a string)
        • get_student_id() → return the student ID
3.In the main program, create one Student object, set its student ID, and print the name and ID.
'''
class Human:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def __str__(self):
        return f"{self.first_name} {self.family_name}"

class Student(Human):
    def __init__(self, first_name, family_name, student_id=None):
        super().__init__(first_name, family_name)
        self.__student_id = student_id

    def set_student_id(self, value):
        if isinstance(value, str):
            self.__student_id = value
        else:
            print ("Student ID must be a string")

    def get_student_id(self):
        return self.__student_id
a=Student("Simone", "North")
a.set_student_id("210010")
print(a, a.get_student_id())
