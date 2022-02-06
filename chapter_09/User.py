class User:
    """Class for users"""
    def __init__(self, first_name, last_name, age):
        """Attributes for users"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Method for descibing a user"""
        print(f"This is {self.first_name.title()} {self.last_name.title()} with age {self.age}")

    def greet_user(self):
        """Method for greeting a user"""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increment attempts of login"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Increment attempts of login"""
        self.login_attempts = 0


first_user = User('David', 'Roude', 45)
first_user.increment_login_attempts()
first_user.describe_user()
first_user.greet_user()
print(first_user.login_attempts)
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(first_user.login_attempts)
first_user.reset_login_attempts()
print(first_user.login_attempts)