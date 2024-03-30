#Abstraction
class Arsenal:
    def ordegard(self):
        print("ordegard")

#polymorphism
        #ability of an object to take on multiple forms
class WHT:
    
    def calc(self):
        WHT = 1000000 * 0.06
        return WHT
value = WHT()
print(value.calc())