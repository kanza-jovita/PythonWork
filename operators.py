#Operators are special characters that tell the computer what to do with the values.
name = "jovita"
#Logic operators and their meaning
#arithmetic operators(+,-/,*//) perfoem arithmetic operations on numbers
num1 = 100
num2 = 200
sum = num1 + num2
print(sum)
#suntraction
sub =  num1 - num2
print(sub)
#multiplication
prod = num1 * num2
print(prod)
#Divide
div = num1 / num2
print(div)
#floor division-when dealing with floor division it rounds off to an integer value
floordiv = num1 // num2
print(floordiv)

#power/expinential
print(num1**2)

#modulo (%) returns the remainder of one number divided by another
print(num1  % num2)

#Assignment operators
num3 = num1 + num2
#this expression below changes the value of num1 from 100 to 102 starting from this line
num1 += 2 #num = num1 + num2
print(num1)

#multiplication assignment
num1 *= 2
print(num1)

#exponentila assignment
num1 **= 2

#modulus assignment
num1 //= 2
print(num1)

num1 %= 2
print(num1)


#comparison operators(tru/false,yes/no,0/1,on/off)
#thes compare two values
comp1 = 100
comp2 = "jovita"
print(comp1 == comp2)#equal
#==(two equal signs) create an assignment operator
#you start with !=
print(comp1 != comp2)#not equal
#greater than/less than comparison
print(num1 < num2)
print(num1 > num2)

#greater tha or equal to
print (10 <= 20)
print(10 >= 20)
#Logical "And" operator
print(True and True)#the conditions are all supposed to be met
print(True and False) 

#Logical "0r" operator
print(True or False)

#Logical "not" operator
print(not True)

#membership operators are in/out 
mylist = [10,20,30,40,50]
print(10 in mylist)#this means is 10 a member in my list
print(100 not in mylist)
print(100 in mylist)

#identity operators-we compare operands than the values itself
mylist2 =[10,20,30,40,50]
print(mylist is not mylist2)
print(mylist is mylist2)

#simple assignment,read about bit-wise operators

#a statement that evaluates to a value is called an expression
#a statement that gives an answer for say is aclled an expression
#a value in programming is called an operand
#an operator is a symbol that tells the computer what to do with the value.
#an operand is what an operator acts upon

#Loops & conditions
#loop-a mechanism through which we can instruct a computer to repeatedly do smthg until the condition is false

