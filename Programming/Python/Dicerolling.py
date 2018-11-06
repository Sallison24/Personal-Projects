""" This program will roll a pair of dice and ask the user to guess the sum of the die. If the user's guess == the total value of the roll, the user wins Other wise the computer wis.

-Author: Scott Allison

"""
from random import randint
from time import sleep

def get_users_guess():
  guess = int(raw_input("Guess a Number: "))
  return guess 
def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides)
  second_roll=randint(1,number_of_sides)
  max_val=number_of_sides*2 
  print "The Maximum value is %d" %max_val
  guess=get_users_guess()
  if guess >max_val:
    print "Please enter in a value less than the Max Value"
  else:
    print "We're rolling the dice....."
    sleep(2)
    print "The first die rolled :%d" %first_roll
    sleep(1)
    print "The second die rolled :%d" %second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total Value is: %d" %total_roll
    print "Results...."
    sleep(1)
    if guess >= total_roll:
      print "Congrats! you beat the machine..."
    else:
      print "The Machines won today..."
  return
roll_dice(20)