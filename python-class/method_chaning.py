# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self



class Car:
    def start(self):
        print("Start the car")
        return self
        
    def brake(self):
        print("Break the car")
        return self
        
    def stop(self):
        print("Stop the car")
        return self
        
    
car = Car()
car.start().brake().stop()