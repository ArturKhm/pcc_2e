import unittest

from city_functions import get_neated_city_name


class MyTestCase(unittest.TestCase):
    def test_city_country(self):
        full_name = get_neated_city_name('Washington', 'dc')
        self.assertEqual(full_name, 'Washington, Dc')


if __name__ == '__main__':
    unittest.main()
