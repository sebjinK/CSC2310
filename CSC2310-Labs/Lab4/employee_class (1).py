class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int):
        self.__first_name = first_name
        self.__last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return self.__first_name + " " + self.__last_name


emp_1 = Employee("John", "Doe", 70000)

print(emp_1.get_full_name()) # We must access the employee's name using a method because the attributes are private.
print(emp_1.salary) # We can access salary directly because the attribute is public.
