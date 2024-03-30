class Animal:
    name = ""
    def eat(self):
        print('I can eat')
#Inheriting from the class animal
        


#this below is a subclass of animal-this is how we inherit.It can aso be called a child class or a derived class.
    # the animal becomes the paraent/super or base.
class Dog(Animal):
    def display(self):
        print('My name is ', self.name)
        print(f'My name is ', {self.name})
gsherph = Dog()
gsherph.name = 'police'
print(gsherph.name)
print(gsherph.display())
print(gsherph.eat())

# assignment create three super classes with there coreesponding sub classes and create aleast two su classes and objects out of them


# class Shoe:
#     name = ""
#     color = ""
#     def lace(self):
#         return 'uses laces'
#     def nolaces(self):
#         return 'uses no laces'

# class Nike(Shoe):
#     def gym(self):
#         return 'for gyming'
#     def party(self):
#         return 'I use them partying'
    
# class Addidas(Shoe):
#     def sneakers(self):
#         return 'I use them for dancing'
#     def boots(self):
#         return 'for rainy seasonings'


# class Bike:
#     name=""
#     warranty=""
#     def twowheeler(self):
#         return "uses 2wheels"
#     def threewheeler(self):
#         return "uses 3wheels"




# class Car:
#     name=""
#     color=""
#     def ctype(self):
#         return 'It is a suv'
     

# class Toyota(Car):
#     def deisel(self):
#         return "Uses diesel"
# primo = Toyota()
# primo.name = "jovita"
# primo.petrol()

# raum = Toyota()
# wish = Toyota()

# class Mitsubishu(Car):
#     def truck(self):
#         return "open roof"
#     def saloon(self):
#         return "covered roof"


#NEW ASSIGNMENT
class Shoe:
    name = ""
    color = ""
    size = ""
    def walk(self):
        return "I use them for exercises"

class Nike(Shoe):
      def display(self): 
           print("This is", self.name)
           print("It is", self.color) 
           print("It is", self.size) 

sneaker = Nike()
sneaker.name =  "Sneakers" 
print(sneaker.name)
sneaker.name = "Air max"
sneaker.color = "black"
sneaker.size = "Medium" 
print(sneaker.display())
print(sneaker.walk())
       

class Addidas(Shoe):
      def display(self): 
           print("This is a", self.name)
           print("It is", self.color) 
           print("It is", self.size)

boot = Addidas()
boot.name = "Boots"
print(boot.name)
boot.name = "boot" 
boot.color = "Brown"
boot.size = "Small"
print(boot.display())
print(boot.walk())



class Instrument:
    name = ""
    color = ""
    size = ""
    def sound(self):
        return "It produces good music"

class Guitar(Instrument):
      def display(self): 
           print("This is an", self.name)
           print("It is", self.color) 
           print("It is", self.size) 

electric  = Guitar()
electric.name =  "Classical_guitar" 
print(electric.name)
electric.name = "epiphone"
electric.color = "black"
electric.size = "Medium" 
print(electric.display())
print(electric.sound())       

class Piano(Instrument):
      def display(self): 
           print("This is a", self.name)
           print("It is", self.color) 
           print("It is", self.size)

digital = Piano()
digital.name = "Digital_piano"
print(digital.name)
digital.name = "kawai" 
digital.color = "Brown"
digital.size = "Small"
print(digital.display())
print(digital.sound())


class Bag:
    name = ""
    color = ""
    size = ""
    def brand(self):
        return "It is the best brand"

class Gucci(Bag):
      def display(self): 
           print("My name is", self.name)
           print("My color is", self.color) 
           print("My size is", self.size) 

suitcase = Gucci()
suitcase.name =  "Suitcases" 
print(suitcase.name)
suitcase.name = "gemini"
suitcase.color = "black"
suitcase.size = "small" 
print(suitcase.display()) 
print(suitcase.brand())      

class Luivitton(Bag):
      def display(self): 
           print("This is", self.name)
           print("It is", self.color) 
           print("It is", self.size)

backpack = Luivitton()
backpack.name = "Backpacks"
print(backpack.name)
backpack.name = "luivitton_speedy" 
backpack.color = "navy blue"
backpack.size = "large"
print(backpack.display())
print(backpack.brand())



