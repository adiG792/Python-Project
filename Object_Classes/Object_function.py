# class/object function gives us the information about the class
# or for modifying the information about the class
from Class_define import Student

student1 = Student("Jim", "Business", 3.1, False)  # student1 is an object
student2 = Student("Adi", "Physics", 3.8, True)  # student2 is an object

print(student2.on_honor_roll())
