
# def vat(rate,price):
#     frate = int((rate/100*price))
#     return frate
#     print(frate)

# def act_price(new_price,old_price):
#     actvat = vat(25,15) + (new_price-old_price)
#     return actvat
#     print(act_price)

# def profit():
#     totalprofit = act_price(40,20)
#     finalprofit = totalprofit + 100
#     print(finalprofit)
# profit()



# #assignmnet 
#     #use to dynamic functions,write two dynamic functions that prompt a user to input ,name,age,email,gendre and it prints them out.
#     #the second function should prompt the user to input the rate of  PAYE(30%),NSSF(11%) and the amount of income(gross slaray) and then calculate the Net pay of an individual
#     #deadline is sunday 9a.m

# def details(name, age, email, gendre):
#     name = input("Enter your name:")
#     print("name is:",name)
#     age = input("Enter your age:")
#     print("age is:",age)
#     email = input("Enter your email:")
#     print("email is:",email)
#     gender = input("Enter your gender:")
#     print("gender is:",gender)

#     # print("Name: ",name)
#     # print("Age: ",age)
#     # print("Email: ",email)
#     # print("Gender: ",gender)
   
# details("name", "age", "email", "gendre")



# def netpay(paye,nssf,gross):
#     gross = int(input("Enter your gross:"))
#     print("gross:",gross)
#     paye = int(input("Enter paye rate(%):"))
#     print("paye rate is:",paye)
#     nssf = int(input("Enter nssf rate(%):"))
#     print("nssf rate is:",nssf)
#     fpay = (int(paye/100 *gross) + int(nssf/100 *gross))
#     netpay = gross - fpay
#     print("netay:",netpay)

#     # print("Gross:",gross)
#     # print("Paye:",paye)
#     # print("nssf:",nssf)
#     # print("Netpay:",gross)

# netpay("paye","nssf","gross")


"""
def name():
    Block of code 
    return statement
    """ 

# def identify(name,age,email,gender):
#     name = input("type you name here")
#     age = input("type you age here")
#     email = input("type you email here")
#     gender = input("type you gender here")
#     print(name,age,email,gender)
#     return [name,age,email,gender]

# print(identify("name","age","email","gender"))


def net_pay(paye,nssf,gross):
   paye = int(input("paye:"))
   nssf = int(input("nssf:"))
   gross = int(input("gross:"))
   nssf1 = (nssf/100) * gross
   print(nssf1)
   paye1 = (paye/100) * gross
   print(paye1)
   net_pay = gross - int(nssf1 + paye1)
   return net_pay
print(net_pay("paye","nssf","gross"))

def net_pay2(paye = int(input("paye: ")), nssf = int(input("nssf: ")), gross = int(input("gross: "))):
   paye1 = (paye/100) * gross
   nssf1 = (nssf/100) * gross
   net_pay = gross - int(nssf1 + paye1)
   return net_pay
print(net_pay2())