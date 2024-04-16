'''
Project Name: python_intro
File Name: employee_class.py
Author: Jacob Strickler
Updated: 10/25/2023
Purpose: Simple Employee class for demonstrating unit tests.
'''


class Employee:
    def __init__(self, first_name: str, last_name: str, office: str, salary: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__office = office
        self.__salary = salary

        self.__full_name = first_name + ' ' + last_name
        self.__email = first_name[0].lower() + last_name.lower() + '@tntech.edu'

    def get_full_name(self):
        return self.__full_name

    def get_email(self):
        return self.__email

    def get_office(self):
        return self.__office

    def get_salary(self):
        return self.__salary

    def change_name(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = first_name + ' ' + last_name

    def move_office(self, new_office: str):
        self.__office = new_office

    def give_raise(self, raise_amount: int):
        self.__salary += raise_amount


emp_1 = Employee('Clark', 'Kent', 'BRWN 210', 70000)

print(emp_1.get_full_name())
print(emp_1.get_email())
print(emp_1.get_office())
print(emp_1.get_salary())

print('Changing Employee Name To: Superman Johnson')
emp_1.change_name('Superman', 'Johnson')
print(emp_1.get_full_name())

print('Moving Office To: BRUN 238')
emp_1.move_office('BRUN 238')
print(emp_1.get_office())

print('Applying $1000 Raise')
emp_1.give_raise(1000)
print(emp_1.get_salary())
