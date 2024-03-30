def add():
    num1,num2 = 10,20
    sum = num1 + num2
    print(sum)
add()

#creating a dynamic function
def add1(num1,num2):
    sum = num1 + num2
    print(sum)

add1(100,50)
add1(200,45)
add1(40,50)

def sub1(num1,num2):
    sub = num1 - num2
    print(sub)
sub1(100,50)

def mul1(num1,num2):
    mul = num1 * num2
    print(mul)
mul1(100,50)

def div1(num1,num2):
    div = num1 / num2
    print(div)
div1(100,50)

def mod1(num1,num2):
    mod = num1 % num2
    print(mod)
mod1(100,50)

def div1(num1,num2):
    div = num1 // num2
    print(div)
div1(100,50)
div1(25,10)

def pow1(num1,num2):
    pow = num1 ** num2
    print(pow)
pow1(100,50)
pow1(60,25)

def exp1(num1,num2):
    exp = num1 ** num2
    print(exp)
exp1(100,50)
exp1(75,50)

def floordiv1(num,num2):
    floordiv = num // num2
    print(floordiv)
floordiv1(100,50)
floordiv1(300,20)

def multidata(num1,num2,name,float):
    print(num1)
    print(num2)
    print(name)
    print(float)
multidata(25,15,"jovita",30.5)


def muiltidata(num1,num2,name,float):
    print(num1,num2,name,float)
muiltidata(25,15,"jovita",30.5)


def data(district,size,float,int):
    print(district)
    print(size)
    print(float)
    print(int)
data("tororo",200,20.5,4)

def hack(name,Yob,district):
    print(name)
    print(Yob)
    print(district)
    current_year = 2024
    age = current_year - Yob
    print(name,"is",age)
hack("kanza",2000,"tororo")



