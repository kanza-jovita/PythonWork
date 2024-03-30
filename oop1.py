#DEFINING AN OBJECT IN PYTHON - we use the key word class followed by the identified name of the class starting with a capital letter and ending with a full colon. 
#a complete set of values to an attribute makes an object

#for example,

class Animal:
    name = ""
    color = ""
    size = ""
    gender = ""
    sound = ""
    species = ""
    age = 0
    def feed(self):
        # print("the animal feeds by chewing")
        return "the animal feeds by chewing"
#a function of a class is called a method and the statements within that method are called behaviours.

#CREATING OBJECTS OF A CLASS ANIMAL.
cat = Animal()
cat.name = "tom"
cat.color = "brown"
cat.size = "meduim"
cat.gender = "male"
cat.sound = "meow"
cat.species = "felime"
cat.age = 10
# cat.feed()
#Accessing objects.
print(f"{cat.name} is {cat.age} years old")
#the features of a class are identified by a dot or access identifier.
#the "f" string helps us to print different data tpyes.

print(cat.name + " does " + cat.sound)
print(cat.name + " is " + str(cat.age), "years old")
print(f"{cat.feed()}")
#we concatenate items of the same dataype for example a string with a string and an integer with an integer.

cow = Animal()
cow.name = "jim"
cow.color = "white"
cow.size = "large"
cow.gender = "female"
cow.sound = "mow"
cow.species = "cow"
cow.age = 20

# print(cow.name + " is " + str(cow.age) + " years old")

# print(f"{cow.name} is " + str(cow.age) + " years old")

goat = Animal()
goat.name = "tim"
goat.color = "gray"
goat.size = "small"
goat.gender = "female"
goat.sound = "bleats"
goat.species = "goat"
goat.age = 20
# print(goat.name + " is " + str(goat.age) + " years old")

#assignment - add aother learning take aways you ahve learnt since the last time and place it in the body  with examples in code.deadline is tomorrow befor class
