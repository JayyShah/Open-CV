import numpy as np 
import scipy

# Sample Matrix

# A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
# print(A)

# Addition

# In order to perform the addition of two matrices A and B, both of them should be of the same
# shape. The addition operation is an element-wise addition done to create a matrix C of the
# same shape as Aand B.


A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
B = np.array([[1,1,1], [1,1,1], [1,1,1]])
C = A+B
print("Sum:",C)

# Substraction

# Similar to addition, subtracting matrix B from matrix A requires both of them to be of the
# same shape. The resulting matrix C will be of the same shape as A and B

A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
B = np.array([[1,1,1], [1,1,1], [1,1,1]])
C = A - B
print("Substraction:",C)


# Multiplication

# Since matrix multiplication depends on the order of multiplication, reversing the order may
# result in a different matrix or an invalid multiplication due to size mismatch.

# A matrix of size (2x3)
A = np.array([[1, 2, 3],[4, 5, 6]])
# B matrix of size (3x2)
B = np.array([[1, 0], [0, 1], [1, 0]])
C = np.dot(A, B) # size (2x2)
print(C)


"""

Matrix Properties

"""

# Transpose Matrix

# When we interchange Columns and rows of a matrix with each other, the resulting matrix is termed as transpose
# matrix and is denoted as A^T for the orginal matrix of A

A = np.array([[1, 2, 3],[4, 5, 6]])
print("Transpose:",np.transpose(A))


# Identity matrix

# This is a special kind of matrix with diagonal elements as 1 and all other elements as zero

I = np.identity(3) # size of identity matrix
print("Identity:",I)


# An interesting property of Identity matrix is that it doesn't modify target matrix after multiplication
# that is  C = AI or C = IA will result in C=I


# Diagonal Matrix

# Extending the definition of an identity matrix, in a diagonal matrix, the entries of a matrix
# along the main diagonal are non-zero and the rest of the values are zero.

A = np.array([[12,0,0], [0,50,0],[0,0,43]])
print("Diagonal:",A)

# Symmetric Matrix

"""
In a Symmetric matrix, the elements follow a property:

a(i,j) = a(j,i). This element wise property for a given symmetric matrix A, can also be defined in terms
of a transpose as A^t = A

"""

# Consider an assymetric matrix (Size nxn)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

# It's transpose can be computed as 

A_T = np.transpose(A)

# Now A+A^T is a symmetric matrix

print("Symmetric:",A+A_T)


# An Anti-Symmetric matrix can be computed as 

# A-A^T = a(i,j) = -a(j,i)

print("Anti-Symmetric",A-A_T)

"""

An important property arises from this; we can break any square matrix into a summation of
symmetric and anti-symmetric matrix.

A = 0.5*(A+A^T) + 0.5 * (A-A^T)

"""

symm = A + A_T
anti_symm = A - A_T
print(0.5*symm + 0.5*anti_symm)

# Trace

# The Trace of a matrix is the sum of all its diagonal elements

A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("Trace:",np.trace(A))

# Determinant 

# Geometrically, the absolute value of a determinant of a matrix is the volume enclosed by
# taking each row as a vector.

A = np.array([[2, 3],[ 5, 6]])
print("Determinant:",np.linalg.det(A))


# Norm of a Matrix

A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print("Norm:",np.linalg.norm(A))

# Inverse of a matrix

# An inverse of a matrix is denoted as A^-1, has an interesting property

# AA^-1 = I = A^-1A. This inverse is unique for each matrix, However, not all matrices have inverse matrices

A = np.array([[1, 2, 3],[5, 4, 6], [9, 8, 7]])
A_inv = np.linalg.inv(A)
print("Inverse matrix",A_inv)

# Now, if we take a product of A and A^-1

print("Product A and inverse A:",np.dot(A, A_inv))


# Computing Eigen Values and Eigen Vectors

# The Eigen value (Lambda) of a square matrix A has the property such that any transformation on it 
# with eigen vector X = the scalar multiplication of (Lambda) with A.


# Ax = Lambda x      where x!=0

# To compute EigenValues and eigen vectors of A:

# | LambdaI - A| = 0     I is an Identity matrix of the same size as A

A = np.array([[1, 2, 3],[5, 4, 6], [9, 8, 7]])
eigvals, eigvectors = np.linalg.eig(A)
print("Eigen Values: ", eigvals)
print("Eigen Vectors:", eigvectors)

# Singular Value Decomposition(SVD)

# SVD is used to perform decomposition of matrix A into USV^-1 , where U and V^-1 are orthogonal
# matrices and S is diagonal matrix

A = np.array([[1, 2, 3],[5, 4, 6], [9, 8, 7]])
U, s, V = np.linalg.svd(A, full_matrices=True)
print("SVD:",U,s,V)




