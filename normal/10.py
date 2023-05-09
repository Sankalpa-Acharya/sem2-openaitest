

l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
if (l*b) > (2*(l+b)):
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")