
# Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today?”
name = "Eric"
print("Hello " + "name "+ "would you like to learn some Python today?")

#Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.
name = "Scovia"
print(name.upper())
names="KATUSABE SCOVIA"
print(names.lower())
print(name.title())


# Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:

famous_person = "Jovita"
print(famous_person + " once said, “A person who never made a mistake never tried anything new.”")


#  Albert Einstein once said, “A person who never made a mistake never 
# tried anything new.”
print(f"{famous_person} once said,A person who never made a mistake never tried anything new")

# Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
# person’s name using a variable called famous_person. Then compose your mes
# sage and represent it with a new variable called message. Print your message.
message = "A person who never made a mistake never tried anything new"
print(message)


# 2-7. Stripping Names: Use a variable to represent a person’s name, and 
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed. 
name = "Nandawula paul"
print("\t Nandawula \n paul")

# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().

print(name.lstrip())
print(name.rstrip())
print(name.strip())

# .File Extensions: Python has a removesuffix() method that works exactly  
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
# filename. Then use the removesuffix() method to display the filename without 
# the file extension, like some file browsers do.

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))



# Restaurant: Make a class called Restaurant. The _init_() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indi
# cating that the restaurant is open.
#  Make an instance called restaurant from your class. Print the two attri
# butes individually, and then call both methods.

class Restaurant:
      def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        return "these are drinks"

open_restaurant = Restaurant("this restaurant is open")
describe_restaurant = Restaurant("montez", "restaurant","black")

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance.
# Users: Make a class called User. Create two attributes called first_name 
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both meth
# ods for each user.