import restaurant
import admin

my_res = restaurant.IceCreamStand('test', 'european')
my_res.describe_restaurant()

my_user = admin.Admin('Derek', 'Sweeny', 26)
my_user.privileges.show_privileges()
