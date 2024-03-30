#define five different classes with atleast shush method taking atleast five parameters and create atleast three different objects out of those.

class House:
    def __init__(self,name,width,type,size,location):
        self.name = name
        self.width = width
        self.type = type
        self.size = size
        self.location = location

House2 = House("flat","500m","flat-topped")


class Car:
    def __init__(self,name,color,warranty,brand,type):
        self.name = name
        self.color = color
        self.warranty = warranty
        self.brand = brand
        self.type = type
        
Car2 = Car("jeep","black","10years")

class  Cloth:
    def __init__(self,name,type,design,color,material,):
        self.name = name
        self.type = type
        self.design = design
        self.color = color
        self.material = material
        
Cloth2 = Cloth("trouser","first-hand","high-waist")

class Animal:
    def __init__(self,name,gender,age,species,size,):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species
        self.size = size
        
Animal2 = Animal("goat","female","10")

class Bird:
    def __init__(self,name,gender,age,species,size):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species
        self.size = size

Bird2 = Bird("eagle","male","15")