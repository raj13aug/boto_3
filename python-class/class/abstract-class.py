
#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation.

# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def run(Self):
        pass
    
    @abstractmethod
    def stop(Self):
        pass
    
class Bus(Vehicle):
    def run(self):
        print("running on bus")
    def stop(Self):
        print("stopping on bus") 
        
class Car(Vehicle):
    def run(self):
        print("running on car")
    def stop(Self):
        print("stopping on car")       
        
        
obj = Bus()
obj.run()
obj.stop()
