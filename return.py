# def age(current_year,yob):
#     age = current_year - yob
#     return age
# age()
# def calc():
#     age1 = age(2024,1962)
#     print(age1)
#     return age1

# calc()


def loan_request():
    loan_amout = input("please enter how much you want:")
    time = input("after how long will you pay:")
    values = [loan_amout, time]
    return values



def pay(amount,time):
    rate =0.05
    pay = amount * rate * time
    return pay



def calculate ():
    ln = loan_request()
    py = pay(20000,5)
    print(py)

calculate()
