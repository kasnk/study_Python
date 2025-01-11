class Employee:
    company="ITC"

    @staticmethod
    def getAbout():
        print("Employee is the base class")
    
class Programmer(Employee): #Single Inheritance
    @staticmethod
    def show():
        print("This is base class Programer")

obj=Programmer()

obj.getAbout()
obj.show()