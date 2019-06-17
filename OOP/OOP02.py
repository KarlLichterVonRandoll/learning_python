class Restaurant(object):

    def __init__(self):
        self.restaurant_name = "KFC"
        self.cuisine_type = "fast food"
        self.number_served = 100

    def describle_restaurant(self):
        print(self.restaurant_name + " with " + self.cuisine_type)

    def open_restaurant(self):
        print("%s is opening" % self.restaurant_name)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


restaurant01 = Restaurant()
# print(restaurant01.cuisine_type)
# restaurant01.describle_restaurant()
# restaurant01.open_restaurant()
# print(restaurant01.number_served)
# restaurant01.increment_number_served(50)
# print(restaurant01.number_served)

