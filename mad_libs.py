"""
This program generates passages that are generated in mad-lib format.
Author: Paulina Gorecka
"""

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs has started!"

name = raw_input("Please,enter your name: ")
adjective_1 = raw_input("Enter an adjective: ")
adjective_2 = raw_input("Another adjective, please: ")
adjective_3 = raw_input("One more adjective: ")
verb = raw_input("Enter a verb: ")
noun_1 = raw_input("Provide a noun: ")
noun_2 = raw_input("Another noun, please: ")
animal = raw_input("Enter a name of an animal: ")
food = raw_input("Food of your choice: ")
fruit = raw_input("Any fruit: ")
superhero = raw_input("Favourite superhero: ")
country = raw_input("Enter the name of a country: ")
dessert = raw_input("Any dessert: ")
year = raw_input("A year of your choice: ")

print STORY % (name, adjective_1, adjective_2, animal, food, verb, noun_1, fruit, adjective_3, name, superhero, name, country, name, dessert, name, year, noun_2)



























