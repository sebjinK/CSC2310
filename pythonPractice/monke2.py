# show loop + print
user_input = int(input("Please enter a number"))

if user_input <= 10:
    print ("Your num is less than or eaqual to 10")
elif user_input > 10:
    print ("YOur num is greater than ten")
elif user_input == 10:
    print ("Your num is equal to ten")

class Employee:
    def __init__(self, firstName: str, lastName: str, salary: int):
        #self is passing the object itsefl to the tfunciton
        self.__firstName = firstName
        self.__lastName = lastName
        self.__salary = salary
    def getSalary(self):
        return self.__salary
        
employee1 = Employee('monkeman', 'Strickler', 10)

print(employee1.getSalary())

# show input and conditionals
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list_1 = my_list[1:6:1]
my_list_2 = my_list[-1:-1:-1] #starts at -1 so it starts at 9
my_list_3 = my_list[-1::-1] #goes backwards through the list 

# inclusive start - if list starts at 1, start at 1
# exclusive end - if list ends with 10 stop before ten
# step - how many times the list iterates