import random


class Die:
    """Class for die and sides"""

    def __init__(self):
        """Initiation"""
        self.sides = 20

    def roll_die(self):
        """Method for rolling a side"""
        print(random.randint(1, self.sides))


# test = Die()
# for i in range(1,11):
#     test.roll_die()
test = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E')
winner = ''
my_ticket = 'A1B2'
active = 1
loop_count = 0
while active == 1:
    for i in range(1, 5):
        winner += str(random.choice(test))
    if winner == my_ticket:
        active = 0
    loop_count += 1
    winner = ''
print(loop_count)
