class Employee:
    """Class for employees"""

    def __init__(self, last_name, first_name, salary):
        """Initialization"""
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def give_raise(self, increment=5000):
        """Method for increasing salary"""
        self.salary += increment


# me = Employee('Art', 'Khm', 1_000_000)
# print(me.salary)

import site;print(site.getsitepackages())