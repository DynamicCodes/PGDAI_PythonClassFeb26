class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 12


s1 = Student("david", 1)
s2 = Student("cdac", 2)


''' you can create object of inner class inside the outer class

OR

you can create object of inner class outside the outter class provided you  use class name to call it'''

s1.lap.brand = "lenovo"
print(s1.lap.brand)
l1 = s1.lap
l1.cpu = "intel"
print(l1.cpu)


lap1 = Student.Laptop()
lap1.brand = "lenovo"
lap1.cpu = "redian"
print(lap1.cpu)
