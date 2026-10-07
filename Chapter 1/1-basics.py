import numpy as np

# 1. Creating arrays
a = np.array([1, 2, 3, 4])
b = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", a)
print("2D Array:\n", b)

# 2. Array properties
print("Dimensions:", b.ndim)
print("Shape:", b.shape)
print("Size:", b.size)
print("Data type:", b.dtype)

# 3. Special arrays
print("Zeros:\n", np.zeros((2, 2)))
print("Ones:\n", np.ones((2, 2)))
print("Identity Matrix:\n", np.eye(3))

# 4. Range and linspace
print("Arange:", np.arange(1, 10, 2))
print("Linspace:", np.linspace(1, 10, 5))

# 5. Indexing and slicing
print("First element of a:", a[0])
print("Slice of a:", a[1:3])
print("Element from 2D array:", b[0, 1])

# 6. Mathematical operations
x = np.array([10, 20, 30])
y = np.array([1, 2, 3])

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)

# 7. NumPy functions
print("Sum:", np.sum(x))
print("Max:", np.max(x))
print("Min:", np.min(x))
print("Mean:", np.mean(x))
print("Square Root:", np.sqrt(x))

# 8. Reshaping
r = np.array([1, 2, 3, 4, 5, 6])
print("Reshaped Array:\n", r.reshape(2, 3))

# 9. Boolean indexing
print("Values > 20:", x[x > 20])

# 10. Random numbers
print("Random floats:", np.random.rand(3))
print("Random integers:", np.random.randint(1, 10, 5))

