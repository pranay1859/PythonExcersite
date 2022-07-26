
class PlayerCharecter:
    # Attrubute
    membership = True

    def __init__(self, name='rando,',age=0):
        if (age > 18):
            self.name = name
            self.age = age
        
    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def addiing_thing(self, num1, num2):
        return num1+num2
    @staticmethod
    def addiing_thing2(num1, num2):
        return num1+num2

    def test(self):
        return self
    
player1 = PlayerCharecter("Nir", 25)

print (player1.test())


