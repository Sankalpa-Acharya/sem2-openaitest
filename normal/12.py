

x = float(input("Input x coordinate of the center of the circle: "))
y = float(input("Input y coordinate of the center of the circle: "))
r = float(input("Input radius of the circle: "))

x_coord = float(input("Input x coordinate of the point: "))
y_coord = float(input("Input y coordinate of the point: "))

# You can use the built-in math module
import math

# Calculate the distance using the Pythagorean Theorem
d = math.sqrt(math.pow((x_coord - x), 2) + math.pow((y_coord - y), 2))

# If d > r, the point is outside the circle
if d > r:
  print("The point is outside the circle.")
# If d = r, the point is on the circle
elif d == r:
  print("The point is on the circle.")
# If d < r, the point is inside the circle
else:
  print("The point is inside the circle.")