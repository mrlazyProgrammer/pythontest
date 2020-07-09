#encoding=utf-8
import restaurant
class IceCreamStand(restaurant.Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["milk","ice","cocolate"]

    def people_flavors(self):
        self.flavors = []
        while True:
            str = input("please input the ice type")
            if str == 'qqq':
                break
            else:
                self.flavors.append(str)
        self.printIce()

    def printIce(self):
        for ice in self.flavors:
            print(ice)

restaurant1 = IceCreamStand('asdsad','feef')
restaurant1.printIce()
restaurant1.people_flavors()


