def add(a,b):
    ans = a+b
    print(ans)

age = 25#is a global variable in the function add1
#functions are a self contained block of code because variables outside the fucntion cannot be accessed by the fuction
#global variables are found outside the function while local variables are found inside the function
def add1(a,b):
    ans = a+b + age
    age1 = 100 #is a local variable in the function add1.
    print(ans)
add1(20,10)
# print(ans) this is outside the function
#the a,b are technically called parameters
#they are the variables we put
#therefore add1 is parametalised function because it has parameters(a function that has parameters)
#the number of parameters is called a parameter list.
#a global variable can be accessed in the function.
#line 5 is called a global cap.
# print(age1) 