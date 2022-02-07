import unittest

from employee import Employee


class MyTestCase(unittest.TestCase):
    """Tests for Employee class"""

    def setUp(self):
        salary = 500_000
        last_name = 'Khm'
        first_name = 'Artur'
        self.me = Employee(last_name, first_name, salary)
        self.increment = 300_000

    def test_give_default_raise(self):
        self.me.give_raise()
        self.assertEqual(self.me.salary, 505_000)

    def test_give_custom_raise(self):
        self.me.give_raise(self.increment)
        self.assertEqual(self.me.salary, 800_000)


if __name__ == '__main__':
    unittest.main()
