class Student:

    def __init__(self, name, major, gpa, is_on_probation):  # when data is passed it is stored in (parameters given)
        self.name = name  # self.(name) = is the actual object name = (name) = the data the user passed in
        self.major = major  # self is referring to actual object
        self.gpa = gpa  # the information that is given by user is stored as an attributes
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
