

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# creating a new tuple
new_tuple = tup1 + tup2
print(new_tuple)

# Update an element of a tuple
new_tuple = new_tuple[:3] + (100,)

print(new_tuple)