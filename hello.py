# clearing the screen
import os
os.system('cls')

# variables
first_name = "Ashish"

print(first_name)

# python data types: 5 major ones are:
# Strings, Numbers, Lists, Tuples, Dictionaries
last_name = "Karki"  # string
age = 32  # number
# list (which is called arrays in most programming languages)
hobbies = ["reading", "watching movies", "running"]

# list vs tuple: lists are mutable - you can add/remove items from it.
# a tuple is immutable
parents = ("Rudra", "Anjana")

favorite_food = {
    "Ashish": "Momo",
    "Rudra": "Popcorn"
}
print(favorite_food)
print(favorite_food["Ashish"])

# string manipulation
my_string = "my name is Ashish Karki"
print(my_string.upper())
print(my_string.swapcase())
print(len(my_string))
print(my_string[5])
print(my_string[3:8])
print(my_string.split(' '))

# lists
first_names = ['Ashish', 'Sushma', 'Dhampu',
               10, 20.5, ['Another list', 'Another item']]
print(first_names)
first_names.append('New item to first names')
print(first_names)
print(len(first_names))

# tuples - not mutable once created
last_names = ('Karki', 'Singh', 'Ping')
print(last_names)
print(last_names[1])
# hack to change a tuple: create a new tuple from existing tuples
last_names_1 = ("Bling",)  # comma at the end is required
last_names_2 = last_names[0:2] + last_names_1
print(last_names_2)

# Dictionaries
fav_pizza = {
    "Ashish": "Hawaian",
    "Puppy": "Chicken BBQ",
    "Golu": "Mixed Meat lovers"
}
print(fav_pizza)
print(fav_pizza["Puppy"])

del fav_pizza["Ashish"]
print(fav_pizza)

fav_pizza["Puppy"] = "Chicken BBQ with Garlic"
print(fav_pizza)

fav_pizza.update({"Ghoompu": "Apple Sauce"})
print(fav_pizza["Ghoompu"])

# comparison operators
print(10 == 10)
print(9 != 10)
print(9 < 10)
print(9 > 10)
print(10 >= 9)
print(first_name == first_names[0])
print(first_names == last_names)

# conditional statements
# If Else Elif
num = 5
if (num > 10) or (num > 9):
    print("greater than 10 or 9")
elif (num > 5) and (num > 4):
    print("greater than 5 and 4 both")
else:
    print("less than 5")

os.system('cls')
# looping
# while loops
counter = 0
while(counter < 10):
    print("The count is %s" % counter)
    counter += 1

# for loops
for x in first_name:
    print(x)

for key, value in fav_pizza.items():
    print("key is %s, value is %s" % (key, value))
