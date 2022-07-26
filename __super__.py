# inheritanche
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("login")
        pass

class Widzard(User):
    def __init__(self, name , power, email):
        # User.__init__ is the way to find __init__ the proper place
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack  Widzard {self.power}')

class Archer(User):
    def __init__(self, name, power, email):
        # super is the way to find __init__ the proper place
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack  Archer{self.power}')

widzard1 = Widzard("A", 150, 'email.com')
archer =  Archer("B", 200, 'email2.com')

print(widzard1.email)
print(archer.email)
print(dir(widzard1))
