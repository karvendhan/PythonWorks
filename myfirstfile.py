# Python beginners language
# Interactive and works on REPL mode
# Object oriented , so it is possible to wrap the functionality as functions of obejects
# Portable language and it can work on numerous platform
print("hello youtubers!")

# Comments are useful by giving the #
mystr="""hello
testing"""
print(mystr)

# variables in python # container in your memeoy to hold the values
var1=55
print(var1)

# Assign values by separator
var1,var2,var3=10,20,'string'
print(var1,var2,var3)

# Possible print functions
print ("Hello World!")
print ("Hello Again")
print ("I like typing this.")
print ("This is fun.")
print ('Yay! Printing.')
print ("I'd much rather you 'not'.")
print ('I "said" do not touch this.')

## Learn the commenting in python
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print ("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print ("This will run.")

# Make the file as UTF-8 Encoding
# - *- coding: utf- 8 - *-

# Numbers and maths
print ("I will now count my chickens:")
print ("Hens", 25 + 30 / 6)
print ("Roosters", 100 - 25 * 3 % 4)
print ("Now I will count the eggs:")
print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print ("Is it true that 3 + 2 < 5 - 7?")
print (3 + 2 < 5 - 7)
print ("What is 3 + 2?", 3 + 2)

print ("What is 5 - 7?", 5 - 7)
print ("Oh, that's why it's False.")
print ("How about some more.")
print ("Is it greater?", 5 > -2)
print ("Is it greater or equal?", 5 >= -2)
print ("Is it less or equal?", 5 <= -2)

# order of operations
#PEMDAS, which stands for Parentheses Exponents Multiplication Division Addition Subtraction

# Variables and Names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

## More variables and printing
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))

## Print variables and its substitution
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

