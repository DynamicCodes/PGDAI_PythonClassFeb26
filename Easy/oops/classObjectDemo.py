'''
class Computer:
    #def __init__(self):   # method overloading not supported in python
        # this is constructor
     #   print("in init")

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def config(self):  # self is the object you are passing
        print("config is", self.name, self.price)



#com1 = Computer()   # a constructor to create a object

#print(type(com1))
#com1.config()
# or use like below
#Computer.config(com1)

com2 = Computer('asus', 3000)
com2.config()
'''


'''
class Computer:
    def __init__(self):
        self.name = 'asus'
        self.price = 1000

    def update(self):
        self.price = 200

    def compare(self, other):
        if self.price == other.price:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
c1.update()
print(c1.price)
print(c2.price)

if c1.compare(c2):
    print("same")
else:
    print("different")
'''


class Student:
    # Class variable (shared by all students)
    school = "ABC School"

    def __init__(self, name, marks):
        # Instance variables (unique for each object)
        self.name = name
        self.marks = marks


# Creating objects
s1 = Student("Rahul", 85)
s2 = Student("Anita", 92)

# Accessing instance variables
print(s1.name, s1.marks)
print(s2.name, s2.marks)

# Accessing class variable
print(s1.school)
print(s2.school)

# changing class variable
Student.school = "Bachelor"
print(s1.school)

# generating seperate variable of school for a object
s2.school = "Master"
print(s1.school)
print(s2.school)

print(Student.school)  # main value will remain same






