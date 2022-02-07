"""Module for admin and privileges"""
import user


class Admin(user.User):
    """Subclass of user"""

    def __init__(self, first_name, last_name, age):
        """Attributes of subclass"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
    #     self.privileges = ['read', 'write']
    #
    # def show_privileges(self):
    #     if len(self.privileges) == 0:
    #         print('There is no privileges')
    #     else:
    #         print("List of privileges:")
    #         for item in self.privileges:
    #             print(f"\t- {item}")


class Privileges:
    """class to store privileges"""

    def __init__(self):
        """Attributes of privileges"""
        self.privileges = ['read', 'write']

    def show_privileges(self):
        """Method"""
        if len(self.privileges) == 0:
            print('There is no privileges')
        else:
            print("List of privileges:")
            for item in self.privileges:
                print(f"\t- {item}")