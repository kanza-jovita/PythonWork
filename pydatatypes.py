#datatypes in python
#numeric
#string
#sequence type
#mapping
#boolean
#set



#Numeric:we have integers(int),float(float),complex numbers(complex)
#examples
num1=10
print(num1, "is of a type", type(num1))
num2=5.0
print(num2, "is of a type",type(num2))
num3=1+2j
print(num3, "is of a type",type(num3))

#type casting
int(num1)
str(num1)
print(num1)


#strings-is a group of characters
name="Jovita" #or'Jovita'
print(name, "is of a type",type(name))
#Semantics refersto the meaning of what you have written
#Type casting-making the computer treate a certaiin data type into another
numx="20"
print(numx, "is of a type",type(numx))
#example of type casting
numy=int(numx)
print(numy,"is a type of",type(numy))
numy=float(numx)
print(numy,"is a type of",type(numy))

#Sequence data types
#under sequence we have lists,tuples and range
#lists is a vriable that can store more than one value
#However,we can store an empty variable list and we store values later on
mylist=[]
mylist.append("Jovita")
print(mylist)
mylist.append(15)
print(mylist)
#append is a specialised command in python used to add values to a list.
#print is a specialised command in python used to output values on a computer screen.
languages=["python","java", "C", "C#","C++", "kotlin","ruby","goland","cobol"]
print(languages[5])
print(languages[5],languages[4])
print(languages[-1],languages[-8])

#tuples are read only elements
#tuples are not mutable
#tuples can store more than one data type

#List/#indexing
country=["uganda","kenya","tanzania",["egypt","somalia",["sudan",["burundi",["Togo"],["Benin"]]]]]
print(country[3][2][0])
print(country[3][-1][-1])
print(country[-1][-1][-1])
print(country[-1][-1][-1][-2][-1])
country.append(10)
print(country)


fruits=["apples","mangoes","oranges",["pawpaws","pears"]]
print(fruits[0])
print(fruits[-1][-1])
print(fruits[0][-2])


#mapping(dictionary)
person={"name":"Jovita", "age":8, "country":"uganda","height":210}
print(person)
print (person.keys())
print(person.values())

#set is unoredered collection of  unique values
student_id={100,200,300,400,500,500}
print(student_id)
print(student_id)

world=[["uganda","kenya","tanzania"],["southafrica","namibia","zambia",["england"]],["tunisia","egypt","libya"],"brazil","USA"]
print(world[-3][-2])
print(world[1][0])
print(world[1][3][0])

uganda = {"name": "uganda", "popn":45,"loc":"eastafrica"}
print(type(uganda))
print(uganda.keys())
print(uganda.values())

my_number = {10,20,30,40,50,40,50}
print(my_number)
#print(my_number)



lakevictoria = {"name:":"victoria","history:":"second largest in world","location:":"uganda","formation:":"downwapping"}
for keys,values in lakevictoria.items():
    print(keys,values)