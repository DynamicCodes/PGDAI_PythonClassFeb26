
class A:

    def __init__(self):
        print("I am init A")
    def feature1(self):
        print("I am f1")

    def feature2(self):
        print("I am f2")


class B(A):

    def __init__(self):    # if you dont have this constructor then B object will call A constructor directly.
        super().__init__()    # will call both constructors
        print("I am init B")

    def feature3(self):
        print("I am f3")

    def feature4(self):
        print("I am f4")


b = B()
