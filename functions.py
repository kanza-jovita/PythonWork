#a named block of code is called a function
#a function is a named group of statments that are related to one another and perform related tasks.
#functions are the building blocks of programming languages
#for example 
#a function is identified by def
def my_function():
    num1,num2 = 20, 40
    print(num1 + num2)
my_function()
#we have two type of functions
#a function created without anything inside the parenthesis(empty parenthesis)(hardcoded values) is called a static function
#while the other is called a dynamic function which has some content inside the parenthesis

#18/03/2024
#We call it a function because it has a full colon at the end of the code.
#Example 1
def condition():
    num = 10
    if num > 0:
        print("num is postive")
    print("the if statement is easy")
#from line 7 to line 10 is called a function definition.
#whatever you put in the body of a fuction is called a function definition.
#when we are creating a function,we are defining a function.
#how do you tell,anything you indent is a function definition.
#a statement that is not part of the code is pushed outside
#condition()
#we have extracted this piece of code from the above 
#Example 2
num = 10
if num > 0:
    print("num is postive")

condition()
#the call of a function is called invoke
#a function is defined a function is invoked.


"""
function condtion(){
this is how a function is written in javascript.
}
"""

def my_condition():
    num = -10#here we are initialising.
    if num > 0:
        print("postive number")
    else:
        print("the number is negative")
    print("this statement is not related to if or else but in the same function")
    #running a file is called to execute.
my_condition()






