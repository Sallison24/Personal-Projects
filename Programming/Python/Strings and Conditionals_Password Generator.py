"""
1.
Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.
For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.
2.
Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.
The letters in the returned list should be unique. For example,
common_letters("banana", "cream")
should return ['a'].
below are the answeres.
"""
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
"""
This second part is a password generator. 
the first portion checks to see if the first name and last name are a certian length. then the slice the sting and create a username. 
the second portion will take a username and take the last character in the username and put it to the front of the list.
"""
def username_generator(first_name,last_name):
  ##username=[]
  if len(first_name)>=3 and len(last_name)>=4:
    first3=first_name[0:3]
    last4=last_name[0:4]
    username=first3+last4
    return username
  else:
    return first_name + last_name
def password_generator(username):
  password=""
  for character in range(0,len(username)):
    password += username[character-1]
  return password  

print(username_generator("Abe","Allison"))
print(password_generator("AbeAlli"))