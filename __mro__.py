#method resolution order


class A:
    numbers = 10
    
class B(A):
    pass

class C(A):
    numbers = 1

class D(B,C):
    pass

print(D.numbers)
print(D.mro())
