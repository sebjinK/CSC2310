import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('John', 'Smith', 'BRWN 215', 70000)

    def tearDown(self):
        pass

    def test_full_name(self):
        self.assertEqual(self.emp_1.get_full_name(), 'John Smith')

    def test_email(self):
        self.assertEqual(self.emp_1.get_email(), 'jsmith@tntech.edu')

    def test_change_name(self):
        self.emp_1.change_name('Bob', 'Ross')
        self.assertEqual(self.emp_1.get_full_name(), 'Bob Ross')

    def test_move_office(self):
        self.emp_1.move_office('BRUN 108')
        self.assertEqual(self.emp_1.get_office(), 'BRUN 108')

    def test_give_raise(self):
        self.emp_1.give_raise(1000)
        self.assertEqual(self.emp_1.get_salary(), 71000)


if __name__ == '__main__':
    unittest.main()
