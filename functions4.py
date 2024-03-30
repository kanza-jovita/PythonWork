#how do we make functions communicate with each other
def vat(rate,price):
    frate = int((rate/100)*price)
    return frate
    # print(frate)
vat(18,20000)

def act_price():
    actvat = vat(18,20000)
    netprice = actvat + 20000
    print(netprice)
act_price()
#a function that wants to share a value must return that value to any value outside the calling function
#the values to the parameters are called arguments for example 18 and 2000
#e.g rate and price are parameters to 18 and 2000 arguments.
#return is the last statement they will execute in a function.

#assignment
#Using parameterlised functions,create three fucntions which share one anothers values and print the last function for example a,b c where a should return to b,b return to c and c prints the last function.
#paste the code in the body of the email.daedline today by 9pm.


#Assignement
#write about your new learning curve with examples.(take aways from last week)
#submitted in through email by 10a.m tomorrow.