## This is a Area Calculator program, this program will ask for user input, specifically a shape for a circle or triangle.Once all input is taken we will out put the area of the given shape.
##--Author Scott Allison.
print "Hello, this is a area calculator prorgram for circles and Triangles"
option = raw_input("What shape's area would you like to calculate? Enter C for Circle or T for Triangle.")
if option=="C":
  radius = float(raw_input("Enter the radius of your Circle: "))
  area= 3.141519 * radius**2 
  print "Area: %f" %area
elif option=="T":
  base = float(raw_input("Enter the base of your Triangle: "))
  height = float(raw_input("Enter the height of your Triangle: "))
  area= 0.5 * base*height 
  print "Area: %f" %area
else :
  print "Please enter a C or T" 