''' polymorphims can be achieved by 4 ways:-
1. DUck typing
2. operator overloading
3. method overloading
4. method overriding

'''
from Easy.oops.inheritance import Mammal

# duck typing
'''
class Pycharm:
    def execute(self):
        print("compiling")
        print("Pycharm is running")

class Myeditor:
    def execute(self):
        print("Myeditor is running")
        print("myeditor is compiling")


class Laptor:

    def code(self, ide):
        ide.execute()


ide = Myeditor()

l = Laptor()
l.code(ide)
'''

'''
# operator overloading

a = 1
b = 2
print(a+b)

print(int.__add__(a,b))

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):       # we're ovreloading the default add operator method
        return Student(self.m1 + other.m1, self.m2 + other.m2)


    def __gt__(self, other): return self.m1 + self.m2 > other.m1 + other.m2



s1 = Student(1,2)
s2 = Student(3,4)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
'''

# method overloading and overriding

# python doesnot have method overloading, but we can trick it to perform
'''primarily due to its dynamic typing system and how it handles namespaces. 
Key Reasons:
Dynamic Typing: In Python, the type of a variable (or function argument) is determined at runtime, not at compile time. Function or method signatures do not depend on the types or the number of parameters explicitly in the way they do in static languages. The interpreter doesn't have the static type information needed to differentiate between multiple methods with the same name but different parameter types at compile time.
Namespace Management (Overwriting): In Python, methods and functions are treated as first-class objects and are stored in a dictionary-like namespace. When you define multiple methods with the same name within the same scope, the later definition simply overwrites the previous one in the namespace. Consequently, only the last defined method is accessible and callable.
"Pythonic" Flexibility: The language's design philosophy favors flexibility over strict, static rules. Python provides alternative mechanisms, such as default arguments, variable-length arguments (*args and **kwargs), and duck typing, which effectively allow a single method to handle varying numbers and types of inputs, achieving a similar goal to method overloading without needing multiple function definitions. '''

class Student():
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None,b=None,c=None):   # trick for method overloading
        if a != None and b != None and c != None:
            return a + b + c
        elif a!=None and b!=None:
            return a + b
        else:
            return 0


s =Student(1,2)
print(s.sum(4,5,5))


# method overriding

class A:

    def show(self):
        print("A show")

class B(A):

    def show(self):     # overriding
        print("B show")


b = B()
b.show()