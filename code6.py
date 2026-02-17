#Shows total café bill matrix after multiplication
import numpy as np

print("Enter 5x3 order matrix:")
A = np.array([list(map(int, input().split())) for _ in range(5)])

print("Enter 3x2 price matrix:")
B = np.array([list(map(int, input().split())) for _ in range(3)])

print("Total Bill Matrix:")
print(np.dot(A, B))
