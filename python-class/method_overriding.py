class Animal():
    def eat(self):
        print("Animal is eatting the food")
        
    
class Rabbit(Animal):
    def eat(self):
        print("Rabbit is eatting the food")
        

obj = Rabbit()
obj.eat()