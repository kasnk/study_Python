class Employee:
    name="Shekhar"
    language="English" #This is an class attribute
    salary=12000000

    def getInfo(self):
        print(self.name)

# Making object
obj=Employee()
obj.address="Sangadi" #This is an object attribute
# print(obj.name,obj.address)
obj.getInfo()
# Note:Class attribute has higher priority


'''
Use 'self' keyword in function argument
in defination
'''