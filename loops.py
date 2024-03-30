#a loop is a mechanism in programming thru which we can istruct a computer to
#repeatedly do something until a certain condition is met

 #range is a keyword in python
#loops are costlt in terms of memory consumption because every iteration requires memory
#two types of loops,that is "for loop" and "while loop".

#for loop
def loop1():
    list = [10,20,30,40,50]
#a loop print out values from alist
#below is an iteration of values in a list of values/numbers
    for i in list:
        print(i)

def loop2():
    for i in range(10):
        print(i)
        item = 1
def loop4():
    for item in range(1,10): #represents the start an 10 represents the end of the list
        print(item)

        for i in range(1,20):
            if i % 2 == 0:
                print(i) #this prints numbers divisable by 2-only even
    
def loop6():
    for i in range(1,20):
        if i % 2 != 0:
            print(i)
#the above code is called a block of code
#a block of code is a collection of related statements
#what shows that a code is a block-its indented,then has a full colon
        
def loop7():
    digits = [20,40,60,80,100]
    for i in digits:
        print(i)  
    else:
        print("no items left")     
        
loop1()





