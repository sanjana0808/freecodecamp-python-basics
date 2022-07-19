from freecodecamp.classes_example.classes_and_objects import Student #importing student from file clasess_and_objects

student1 = Student("Jim", "Business", 2.1, False)
student2 = Student("Tom", "Finance", 4, True)

print(student1.name)
print(student1.major)

print(student1.brilliant_student())
print(student2.brilliant_student())