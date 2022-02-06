class Restaurant:
    """A class for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Return a description of the resraurant"""
        print(f"This is a restaurant called {self.restaurant_name} with cousine type {self.cuisine_type}")

    def open_restaurant(self):
        """Return a message that the restaurant is open"""
        print(f"{self.restaurant_name.title()} is open")

    def set_number_served(self, new_number):
        """Set number served"""
        self.number_served = new_number

    def increment_number_served(self, increment):
        """Increment number served by increment"""
        self.number_served += increment


my_restaurant = Restaurant('ArtRes', 'european')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_second_res = Restaurant('Second', 'asian')
my_third_res = Restaurant('Third', 'african')
# my_list = [my_restaurant, my_second_res, my_third_res]
# for res in my_list:
#     print(res.describe_restaurant)
my_restaurant.describe_restaurant()
my_second_res.describe_restaurant()
my_third_res.describe_restaurant()

print(my_restaurant.number_served)
my_restaurant.number_served = 10
print(my_restaurant.number_served)
my_restaurant.increment_number_served(6)
print(my_restaurant.number_served)
