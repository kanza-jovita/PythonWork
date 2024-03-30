#Assigns the string "Python is fun" to the variable some_string.
some_string = 'Python is fun' 
#a, b, c = 5, 3.2, 'Hello' assigns the values 5, 3.2, and 'Hello' to the variables a, b, and c, respectively.
a, b, c = 5, 3.2, 'Hello'

print(a)  #Displays the value stored in variable a, which is 5.
print(b)  #Displays the value stored in variable b, which is 3.2.
print(c)  #Displays the value stored in variable c, which is 'Hello'

#Assigning the integer value 5 to the variable num1.
num1 = 5
#Displays the value of num1, which is 5, and also shows its type using the type() function, which returns int. So, the output will be: 5 is of type <class 'int'>.
print(num1, 'is of type', type(num1))
#Assigns the floating-point number 2.0 to the variable num2.
num2 = 2.0
#Displays the value of num2, which is 2.0, and its type, which is float. So, the output will be: 2.0 is of type <class 'float'>.
print(num2, 'is of type', type(num2))
#Assigns a complex number 1+2j to the variable num3.
num3 = 1+2j
#Displays the value of num3, which is 1+2j, and its type, which is complex. So, the output will be: (1+2j) is of type <class 'complex'>.
print(num3, 'is of type', type(num3))
#Creates a list named languages containing three strings: "Swift", "Java", and "Python"
languages = ["Swift", "Java", "Python"]

#Displays the first element of the languages list to the console.
print(languages[0])   # #Swift

#Displays the third element of the languages list to the console.
print(languages[2])   #  Java

#Creates a tuple named product with three elements 'Microsoft','Xbos', 499.99.
product = ('Microsoft', 'Xbox', 499.99)

#Displays the first element of the tuple product.
print(product[0])   # Microsoft

#Displays the second element of the tuple product.
print(product[1])   # Xbox


#Creates a dictionary named capital_city.So, capital_city is a dictionary where country names are keys and their corresponding capital cities are values.
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#It will output the entire dictionary capital_city,{'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)


#Creates a set named student_id.
student_id = {112, 114, 116, 118, 115}

#Will display the content of the set student_id,{112, 114, 115, 116, 118}
print(student_id)

#Uses the type() function to determine and print the type of the variable student_id.
#<class 'set'>
print(type(student_id))

#This defines a list named fruits containing three strings: "apple", "mango", and "orange".
fruits = ["apple", "mango", "orange"] 
#This will display the list fruits as it is, including the square brackets and commas separating the elements.['apple', 'mango', 'orange']
print(fruits)

#This defines a tuple named numbers containing three integers: 1, 2, and 3
numbers = (1, 2, 3) 
#Displays the tuple numbers (1, 2, 3)
print(numbers)

#This defines a dictionary named alphabets with keys as letters of the alphabet and corresponding values as words starting with those letters.
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#Displays the dictionary alphabets.{'a': 'apple', 'b': 'ball', 'c': 'cat'}
print(alphabets)

#A set named vowels which outputs {'a', 'e', 'i', 'o', 'u'}
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# This is  creating a variable named student_id and assigning it a set containing five elements: 112, 114, 116, 118, and 115.
student_id = {112, 114, 116, 118, 115}

#Displays the values of student_id,{112, 114, 115, 116, 118}
print(student_id)

# Displays the type of the variable student_id. <class 'set'>
print(type(student_id))
#Defines a tuple named product where product is a tuple representing information about a Microsoft Xbox, including the brand, model, and price.
product = ('Microsoft', 'Xbox', 499.99)

#Outputs the first element of the tuple product, which is 'Microsoft'
print(product[0])   # Microsoft

# Outputs the first element of the tuple product, which is 'Xbox'
print(product[1])   # Xbox




#Here, two variables a and b are being assigned values 7 and 2
a = 7
b = 2

#Outputs 'Sum: ' followed by the result, which is 9. 
print ('Sum: ', a + b)  

#Displays 'Subtraction: ' followed by the result, which is 5
print ('Subtraction: ', a - b)   

#Displays 'Multiplication: ' followed by the result, which is 14 
print ('Multiplication: ', a * b)  

#Displays 'Division: ' followed by the result, which is 3.5.
print ('Division: ', a / b) 

#Displays 'Floor Division: ' followed by the result, which is 3
print ('Floor Division: ', a // b)

#Displays 'Modulo: ' followed by the result, which is 1.  
print ('Modulo: ', a % b)  

#Displays 'Power: ' followed by the result of a ** b, which is 49 
print ('Power: ', a ** b)   


# a = 10 assigns the value 10 to the variable a.
a = 10

#b = 5 assigns the value 5 to the variable b. 
b = 5 

# 
a += b      #Adds the value of b to the value of a and assigns the result back to a. 
print(a)
# Output:  15


#Displays the string 'a == b =' followed by the result False,a == b = False.
print('a == b =', a == b)

#Displays a != b = True. This indicates that a is not equal to b.
print('a != b =', a != b)

#Displays whether the value of variable a is greater than the value of variable b,a > b = True 
print('a > b =', a > b)

#Displays whether the value of variable a is less than the value of variable b,a < b = False
print('a < b =', a < b)

#Displays whether the value of variable a is greater than or equal to the value of variable b,a >= b = True
print('a >= b =', a >= b)

#Displays whether the value of variable a is less than or equal to the value of variable b,a <= b = False
print('a <= b =', a <= b)
#Checks if a is greater than 2 and if b is greater than or equal to 6,False
print((a > 2) and (b >= 6)) 

#Logical AND
print(True and True)     #This will output True because both operands are True.
print(True and False)    #This will output False because one of the operands (the second one) is False.

# logical OR
print(True or False)     #When you print True or False, the result will be True because the or operator returns True if at least one of its operands is True. Since the first operand is True, the expression evaluates to True.

#Logical NOT
print(not True)          #Here the result will be False because not operator negates the boolean value of its operand, so not True evaluates to False.


#These are pairs of variables that reference the same objects due to the immutability (for integers and strings) and mutability (for lists) of the objects they are assigned to.
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
#Checks whether x1 and y1 are not referring to the same object in memory.
print(x1 is not y1)  # False

#Checks if the two variables x1 and y1 refer to the same object in memory.
print(x2 is y2)  #True.

#Checks whether the variables x3 and y3 refer to the same object in memory.
print(x3 is y3)  #True

#Assigns the string 'Hello world' to the variable message
message = 'Hello world'

#Initializes a dictionary named dict1 with two key-value pairs.
dict1 = {1:'a', 2:'b'}

#Checks if the character 'H' is present in the variable message, and then displays the result of this check.
print('H' in message)  #True

#Checks whether the string 'hello' is not present in the variable message, and then displays the result of this check.  
print('hello' not in message)  #True

#This  is attempting to determine if the key 1 exists in the dictionary dict1.
print(1 in dict1)  #True

#Checks whether the key 'a' exists within the dictionary dict1. 
print('a' in dict1)  #False