
class Student:

    school = 'cdac'  # class variable

    def __init__(self, m1,m2,m3):
        self.m1 = m1                 # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):    # instance method, because we pass self
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):      # getter are called accessor
        return self.m1

    def set_m1(self, value):
        self.m1 = value     # setters are called mutators


    # class method, use cls for class, self for instance
    @classmethod   # this is decorator, use to define class method
    def get_school_name(cls):
        print(cls.school)


    # static method
    @staticmethod
    def info():
        print("this is student class info")



s1 = Student(1,2,3)
s2 = Student(4,5,6)

print(s1.avg())
Student.get_school_name()
Student.info()
