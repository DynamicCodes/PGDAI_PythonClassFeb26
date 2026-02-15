'''
class A:
    def feature1(self):
        print("I am f1")

    def feature2(self):
        print("I am f2")


class B(A) :    # child class ,,  single inheritance
    def feature3(self):
        print("I am f3")

    def feature4(self):
        print("I am f4")

class C(B):    # multilevel
    def feature5(self):
        print("I am f5")


# multiple inheritance



class D(A,B):
    def feature6(self):
        print("I am f6")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()

d1 = D()
d1.feature6()
d1.feature5()
'''

'''
# multiple inheritance with Method Resolution Order (MRO)
class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m() # Calls the next method in the MRO

class C(A):
    def m(self):
        print("m of C called")
        super().m() # Calls the next method in the MRO

class D(B, C):
    def m(self):
        print("m of D called")
        super().m() # Calls the next method in the MRO

x = D()
x.m()

'''

class Animal:
    def speak(self): print("Animal sounds")

class Mammal(Animal):
    def speak(self):
        super().speak()
        print("Mammal sounds")

class Winged(Animal):
    def speak(self):
        super().speak()
        print("Winged sounds")

class Bat(Mammal, Winged):
    def speak(self):
        super().speak()
        print("Bat sounds")

b = Bat()
b.speak()

'''the out is 
Animal sounds
Winged sounds
Mammal sounds
Bat sounds

because super follows mro= Bat → Mammal → Winged → Animal

Now the Stack Unwinds

After Animal, execution returns upward:

Winged prints → "Winged sounds"

Mammal prints → "Mammal sounds"

Bat prints → "Bat sounds"'''




