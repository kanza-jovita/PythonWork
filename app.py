name = input('what is your name? ')
color = input('what is you favourite color? ')
print(name + ' likes blue')


birth_year = input("enter you birth year")
age = 2020 - int(birth_year)
print(age)


first = input("first")
second = input("second")
sum = first + second
print(sum)

#IF STATMENTS
temperature = 25
if temperature > 30:
    print("it's a hot day")
    print("drink plenty of water")
elif temperature > 20:
    print("it's a nice day")
elif temperature > 10:
    print("it's a bit cold")
else:
    print("it's cold")
print("done")


weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))

else:
    converted = weight * 0.45
    print("weight in Kgs: " + str(converted))

#WHILE LOOPS
i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

names = ["john","bob","mosh"]
names[0] = "Jon"
print(names[0])
print(names[-1])
print(names[-2])
print(names[0:3])

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

numbers = [1,2,3,4,5]
numbers.insert(0,-1)
print(numbers)

numbers = [1,2,3,4,5]
numbers.remove(3)
print(numbers)

numbers = [1,2,3,4,5]
numbers.clear()
print(numbers)


numbers = [1,2,3,4,5]
print(1 in numbers)

numbers = [1,2,3,4,5]
print(len(numbers))


numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1





