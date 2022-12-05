import numpy as np 
import  scipy

"""
A vector is denoted by a One-Dimensional Array
p = [1,2,3]

The common properties required are length and Magnitude of Vector
print(len(p))

-------------------------------------------------------------------------

Common Vector Operations are:

Addition
Subtraction
Vector multiplication
Vector norm
Orthogonality

-----------------------------------------------------------------------------

"""

# Addition

v1 = np.array([2,3,4,5])
v2 = np.array([4,5,6,7])

print("Addition:",v1+v2)


# Substraction

v1 = np.array([2,3,4,5])
v2 = np.array([4,5,6,7])

print("Substraction:",v1-v2)

# Multiplication

# There are two methods for Vector Multiplication
# * Inner Product - AKA Dot product and is the sum of element vise product of two vectors
# * Outer Product - This takes two vectors and computes a matrix
# Check images of Inner product and Outer product in the images folder


# Inner Product

v1 = np.array([2, 3, 4, 5])
v2 = np.array([4, 5, 6, 7])
print("Inner Product:",np.inner(v1, v2))

# Outer Product

v1 = np.array([2, 3, 4, 5])
v2 = np.array([4, 5, 6, 7])
print("Outer Product:",np.outer(v1, v2))

# Vector Norm
# Check the images folder for Norm, L1 and L2 norms

# L1-Norm

v = np.array([2, 3, 4, 5])
print("L1-Norm:",np.linalg.norm(v, ord=1))

# L2-Norm

v = np.array([2, 3, 4, 5])
print("L2-Norm:",np.linalg.norm(v, ord=2))

# Orthogonality

# Two vectors are said to be orthogonal if their inner product is zero. From the geometric point
# of view, if the two vectors are perpendicular, they are said to be orthogonal to each other:

v1 = np.array([2, 3, 4, 5])
v2 = np.array([1,-1,-1,1]) # orthogonal to v1
print("Orthogonality:",np.inner(v1, v2))