class User:
    """Class for users"""
    def __init__(self, first_name, last_name, age):
        """Attributes for users"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Method for descibing a user"""
        print(f"This is {self.first_name.title()} {self.last_name.title()} with age {self.age}")

    def greet_user(self):
        """Method for greeting a user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


first_user = User('David', 'Roude', 45)
first_user.describe_user()
first_user.greet_user()
