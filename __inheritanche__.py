# inheritanche
class User:
    def sign_in(self):
        print("login")
        pass

class Widzard(User):
    def __init__(self, name , power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack  Widzard {self.power}')

class Archer(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack  Archer{self.power}')

widzard1 = Widzard("A", 150)
archer =  Archer("B", 200)

widzard1.attack()

print(isinstance(widzard1, Widzard))
print(isinstance(widzard1, User))
print(isinstance(widzard1, object))