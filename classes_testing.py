# working with classes

#Class Snowboard
class Snowboard:

    #Class variables
    length = 0
    make = ''
    model = ''
    width = 0

    #Init method or constructor
    def __init__(self, length, make, model, width,):
        #Instance Variables
        self.length = length
        self.make = make
        self.model = model
        self.width = width

    def print_details(self):
        print(f"This is a {self.length} {self.make} {self.model}")

    def ollie(self):
        print("Niiice ollie!")

    def spin(self):
        print("Sweet spins!")

#Instantiate a snowboard
MySnowboard = Snowboard(152,'Never Summer','Proto Type Two',30)

#Let's do some methods!
MySnowboard.print_details()
MySnowboard.ollie()
MySnowboard.spin()
MySnowboard.spin()
