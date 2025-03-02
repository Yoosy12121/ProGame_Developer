
class Student():
    #properties/ attributes
    name = ""
    age = 12
    schoolclass = "Year 7 "
    house = "Sapphire"
    classteacher = "Mr Speake"

    #constructor
    def __init__(self):
        print("Making a new student")

    #Another Function
    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print ("Please enter the name of the student")
        self.name = input()

    #Another Function
    def show_Details(self):
        print("The details of student are:")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)
    
#Student class definition  is over
#Making 2 objects/ instances of Student class
Yusuf = Student()
Surabhi = Student()

Yusuf.change_details()
Surabhi.show_Details()