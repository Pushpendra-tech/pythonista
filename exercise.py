class Dog():
    
    species = 'mammal'
    
    def __init__(self,mybreed,name):
        self.breed=mybreed
        self.name = name
        
    def bark(self):
        print("woof my name is {}".format(self.name))

mydog = Dog('lab','bob')
print(mydog.species)
print(mydog.bark())
print(mydog.breed)
