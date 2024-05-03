from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper


class TestDbHelper(TestCase):

    @patch('src.db_helper.DbHelper')
    def test_get_maximum_salary_with_mocking(self, MockDbHelper):
        db_helper = MockDbHelper()  # create a mock object of DbHelper class
        db_helper.get_maximum_salary.return_value = "60000"
        actual = db_helper.get_maximum_salary()
        expected = "60000"
        self.assertEqual(actual, expected)

    @patch('src.db_helper.DbHelper')
    def test_get_minimum_salary_with_mocking(self, MockDbHelper):
        db_helper = MockDbHelper()       # create a mock object of DbHelper class
        db_helper.get_minimum_salary.return_value = "50000"
        actual = db_helper.get_minimum_salary()
        expected = "50000"
        self.assertEqual(actual, expected)

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
        db_helper = MockDbHelper()  # create a mock object of DbHelper class
        db_helper.get_maximum_salary.return_value = 60000
        db_helper.get_minimum_salary.return_value = 50000

        max_salary = db_helper.get_maximum_salary()
        min_salary = db_helper.get_minimum_salary()
        self.assertGreater(max_salary, min_salary)