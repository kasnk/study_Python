class Sample:
    name="Aman"
    salary=120000

    @staticmethod
    def __init__(name,salary): #Dunder Method,which is automatically called
        print("I am creating an object!")
        print(name,salary)

    @staticmethod
    def getInfo():
        print(obj.name,obj.salary)

obj=Sample("Shekhar",1300)
obj.getInfo()
