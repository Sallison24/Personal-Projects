""" this is my trip planner script, it calculates the cost of a trip to four cities, and how many days you'll stay
-Author Scott Allison"""



def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = 40 * days
  if days >=7:
  	 cost -=50
  elif days >=3:
  	 cost -=20
  return cost

def trip_cost(city,days,spending_money):
  return rental_car_cost(days)+hotel_cost(days - 1)+plane_ride_cost(city)+spending_money

""" In my free time I want to add in user input to ask which city they want to go
too """
print trip_cost("Los Angeles",5,600)