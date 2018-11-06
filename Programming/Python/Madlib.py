"""
This is a madlibs program, this program will ask for user input, and once all input is taken, output a full story

--author Scott Allison. 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
print' Welcome to my first python Madlibs'
name=raw_input("Enter a name: ")
adj1=raw_input("Enter an Adjetive: ")
adj2=raw_input("Enter an Adjetive: ")
adj3=raw_input("Enter an Adjetive: ")
verb1=raw_input("Enter an Verb: ")
noun1=raw_input("Enter an Noun: ")
noun2=raw_input("Enter an Noun: ")
animal=raw_input("Enter an Animal: ")
food=raw_input("Enter a type of food: ")
fruit=raw_input("Enter a fruit: ")
supper1=raw_input("Enter an Superhero: ")
country=raw_input("Enter an Country: ")
dessert=raw_input("Enter an dessert: ")
year=raw_input("Enter an year: ")
print STORY % (name,adj1,adj2,animal,food,verb1,noun1,fruit,adj3,name,supper1,name,country,name,dessert,name,year,noun2)

