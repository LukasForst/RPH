import math

class MyVector:
    possible = False

    def __init__(self, x):
        self.x = x
        if(type(self.x) != list):
            self.possible = False
            raise ValueError("Wrong type = it's not list " + str(type(self.x)))
        else:
            self.possible = True

    def get_vector(self):
        return self.x

    def __add__(self, other):
        self.added = []
        for i in range(len(self.x)):
            self.added.append(self.x[i] + other.x[i])
        return MyVector(self.added)

    def norm(self):
        mezivypocet = 0
        for i in range(len(self.x)):
            mezivypocet += self.x[i]*self.x[i]
        self.normed = math.sqrt(mezivypocet)
        return self.normed

if __name__ == "__main__":
    a = MyVector([1])
    b = MyVector([2])
    c = a+b
    print(type(c))
    print(c.get_vector())
    print(MyVector([1]).norm())
    print(MyVector([3,4]).norm())
    print(MyVector([1,1,2**0.5]).norm())

