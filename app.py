from vector import Vector

my_vector = Vector([1, 2, 3])
print my_vector

my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])
my_vector4 = Vector([1.996, 3.108, -4.554])

#this will return True
print my_vector == my_vector2

#this will return False
print my_vector == my_vector3

print my_vector4.magnitude()