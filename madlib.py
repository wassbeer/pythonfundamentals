"""
This program will prompt the user for input and will output the entire Mad Libs story with the user's input in the right place
"""

print("Mad Libs has started!")

name = input("Enter a name: ")

# adjectives

jj1 = input("Enter an adjective: ")
jj2 = input("Enter another adjective: ")
jj3 = input("Please, provide a third and final adjective: ")

# verbs

vb1 = input("Enter a verb: ")
vb2 = input("Enter another verb: ")
vb3 = input("Please, provide a third and final verb: ")

# nouns

nn1 = input("Enter a noun: ")
nn2 = input("Enter another noun: ")
nn3 = input("Please, provide a third and final noun: ")

# funitems

animal = input("Enter an animal: ")
food = input("Enter a type of food you like: ")
fruit = input("Enter a fruit you like: ")
number = input("Enter a random number: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

# The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."

# formatting

print(STORY % (jj1, name, vb1, jj2, nn1, country, superhero, fruit, vb2, nn2, animal, jj3,
               superhero, vb2, jj1, superhero, name, name, fruit, dessert, food, nn3, name, year, animal))
