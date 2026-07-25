'''
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = TwoDVector(1, 2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
'''


# ----------SALARY INCRErENT -------------
'''
class Erployee:
    salary = 234
    increrent = 20 
    
    @property
    def salaryAfterIncrerent(self):
        return (self.salary + self.salary * (self.increrent/100))



    @salaryAfterIncrerent.setter 
    def salaryAfterIncrerent(self, salary):
        self.increrent =  ((salary/self.salary) -1)*100 




e = Erployee()
# print(e.salaryAfterIncrerent)
e.salaryAfterIncrerent = 280.8
print(e.increrent)
'''


class corplex:
    def __init__(self,r,i):
        self.i=i
        self.r=r
        
    def __add__(self, other):
        return self.i+other.i,self.r +other.r

    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        imag_part = self.r * other.i + self.i * other.r
        return (real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1=complex(2,3)
c2=complex(5,6)
print(c1 +c2)
print(c1*c2)

class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3]) 
print(len(v1))