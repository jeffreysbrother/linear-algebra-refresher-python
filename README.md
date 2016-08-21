#Linear Algebra Refresher

Fundamental objects: **points** and **vectors**.
A vector is an object that represents a change in position. In Euclidean space, a vector can be conceived of as an arrow connecting two points. A vector (in Eucliden space) has two important properties: magnitude and direction. Vectors do not have a fixed location; two vectors are equivalent if they represent the same amount of change in some direction.

###Operating on Vectors

To visualize the sum of two vectors (in a geometric fashion), imagine them as lying end-to-end. The arrow formed at the tail of the first and ending at the head of the second makes clear the overal amount of change of the two vectors. This is the sum of the first two vectors.

There is also a numeric interpretation of vector addition. We can add the corresponding coordinates of each vector. 

In order to visualize vector subtraction, position two vectors as emanating from the same point. What vector would we need to add to the bigger (the more severe or bigger or comparatively magnitudinous?) in order for the sum to be that of the smaller?

And similarly for scalar multiplication. We can "scale" the size of a vector by multiplying by two (in so doing, doubling its length), by multiplying by 1/2 (cutting its length in half), or by multipying by a negative (which would reverse the direction of the vector).


###Magnitude and Direction

The magnitude of v is the square root of the sum of the squares of its coordinates. 

A unit vector is a vector whose magnitude is 1. A vector's direction can be represented by a unit vector. The process of finding a unit vector pointing in the same direction as a given vector is called "normalization". This normalization process has two steps: 1) find its magnitude. 2) perform a scalar multiplication: multiply v by the number 1/||v||. This scales the vector up or down so that its length becomes 1.

If all the coordinates of a vector is 0, we call that vector the zero vector. This is a vector indicating no change. The magnitude of the zero vector is zero. What happens if we try to normalize the zero vector? We can't divide by zero, so we say that the zero vector has no normalization; the zero vector has no direction.