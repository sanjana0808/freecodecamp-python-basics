# Definition: A class is a blueprint/template/prototype
# that defines the variables and methods common to all objects of a certain kind.

# My definition of CLASS = A group of information about an object is called a CLASS.
# My definition of object = Actual values which are passed into a class

class Student: #in a class__init__ function contains an argument self
    age = 5
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def brilliant_student(self):
        if self.gpa >= 3:
            return True
        return False