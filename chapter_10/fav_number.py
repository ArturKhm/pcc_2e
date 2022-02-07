import json


def store_number(number):
    """Function to store number"""
    with open('fav_num.txt', 'w') as f:
        json.dump(number, f)
    return number


def get_stored_number():
    """Function to get stored number"""
    try:
        with open('fav_num.txt') as f:
            number = json.load(f)
    except FileNotFoundError:
        number = None
    return number


number = get_stored_number()
if number:
    print(number)
else:
    number = input('Give a number')
    store_number(number)
    print(f"{number} is stored")

# number = input('Give your favorite number: ')
# with open('fav_nub.txt', 'w') as f:
#     json.dump(number, f)
# with open('fav_nub.txt') as f:
#     number = json.load(f)
# print(number)
