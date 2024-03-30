#The following are my key take aways from the previous classes.

#OOP-OBJECT ORIENTED PROGRAMMING
#Object Oriented programming is a paradigm of software development that advocates for developing software based on real world objects.
#The steps on how to solve a problem is called an algorithm.

#Principles of Object Oreinted Programming
    #polymorphism
    #Inheritance
    #Abstraction
    #Encapsulation

#A class is a blueprint of an object(the origanl copy of something)e.g class car has objects such a benz,toyota,range rovers,class phone has objects such a itel,nokia,samsung,iphone,etc.
#Objects take on all features of a class but each object has different attributes /features of the class.

#An object is an instance of a class.
#A class is also a block of code.

#A class can have 10 varialbles each item that completes those 10 variables is complete and is called an object for example we have a class,animal with attributes name, color, number of legs therefore a complete set of those values is called an object.

#We use "is a" to identify a class of an object e.g lake victoria 'is a' lake therfore lake is the class and lake victoria is the object.

#Abstraction refers to ability to ignore other details and concentrate on the highest level of representation
#Abstract helps in identifying classes.
#Class names are always in singular e.g class "car" not "cars".

#Inheritance is the ability by an object to take on different attributes from different classes for example toyota wish is belonging to a class toyota and a class car,subaru legacy is an instance belonging to subaru and class car
#we can have a class in a class.


#Polymorphism is having the ability by an object of a class to take on differnt forms/attrbutes.

#Encapsulation (privacy and independance) is the ability to have what to share and what not to share.

#To identify an object,we use the key word class followed by the identified name of the class starting with a capital letter and ending with a full colon. 
#A complete set of values to an attribute makes an object.

#for example,

class Bird:
    name = ""
    color = ""
    size = ""
    gender = ""
    sound = ""
    def feed(self):
        return "the bird feeds by pecking"
#A function of a class is called a method and the statements within that method are called behaviours.
#The features of a class are identified by a dot or access identifier.
dove = Bird()
dove.name = "shay"
dove.color = "white"
dove.size = "small"
dove.gender = "male"
dove.sound = "wiiwii"
dove.age = 17

print(f"{dove.name} is {dove.age} years old")
print(dove.name + " does " + dove.sound)
print(dove.name + " is " + str(dove.age), "years old")
print(f"{dove.feed()}")
