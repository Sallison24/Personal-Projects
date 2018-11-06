def cube(number):
  return number*number*number 
def by_three(number):
  if number % 3 ==0:
    cube(number)
  else number % 3 != 0:
    return False
