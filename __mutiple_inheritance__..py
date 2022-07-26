# inheritanche
class User:
    def sign_in(self):
        print("login")

class Widzard(User):
    def __init__(self, name , power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack  Widzard {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attack  Archer{self.power}')
    
    def check_arrow(self):
            print(f'{self.arrows} remaining')
    
    def run(self):
        print(f'run really fast')

class HybridBrog(Widzard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name , arrows)
        Widzard.__init__(self, name, power)

hb1 = HybridBrog('brogie', 50, 100)
print(hb1.check_arrow())
print(hb1.attack())
print (hb1.run())