class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def get_oldest_cat(*args):
    print (type(args))
    return max(args)

# 1 Instantiate the Cat object with 3 cats
cat_one = Cat("a",10)
cat_two = Cat("b",20)
cat_three = Cat("c", 30)
# 2 Create a function that finds the oldest cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The oldest cat is {get_oldest_cat(cat_one.age, cat_two.age, cat_three.age)} years old.")