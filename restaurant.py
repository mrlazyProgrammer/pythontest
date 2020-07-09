class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restanrant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\n" + self.restanrant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restanrant_name + " is open!")


