
'''class calculator:
    def __init__(self, n):
        self.n = n

    def cube(self):
        print(f"the cube of n is{self.n*self.n*self.n} ")

    def square(self):
        print(f"the square of  n is {self.n*self.n} ")

    def square_root(self):
        print(f"the square root of n is {self.n**1/2}")
    @staticmethod
    def helo():
        print ( "Hello there ! ")


c = calculator(4)
c.helo()
c.square()
c.cube()
c.square_root()


class Demo:
    a = 4


o = Demo()
print(o.a)  # Prints the class attribute because instance attribute is not present
o.a = 0  # Instance attribute is set
print(o.a)  # Prints the instance attribute because instance attribute is present
print(Demo.a)  # Prints the class attribute
'''

class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1 

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2 

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


o = Manager()
print(o.a, o.b, o.c)

# -----------------CLASS METHOD-------------
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

# ----------------PROPERTY DECORATER & SETTER-----------
class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Harry Khan"
print ( e.name)
print(e.fname)
print(e.lname)
print(e.fname,"\n",e.lname)

e.show()

# ------------OPERATOR OVERLOADING -----------
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

n = Number(1)
m = Number(2)

print(n + m)