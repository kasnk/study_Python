class Demo:
    name="Shekhar"
    address="Sangadi"

    @staticmethod
    def greet():
        print("Good Morning!")

    @staticmethod
    def getInfo():
        print(obj.name,obj.address)
obj=Demo()
obj.greet()
obj.getInfo()


"""
To avoid the 'self' keyword use 
@staticmethod always
It is known as decorator
"""