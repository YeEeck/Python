from numpy import *

m1 = mat([[2, 0, 1], [-1, 0, 3], [1, -2, 1]])
m2 = mat([[-2, 1, 1], [-8, 1, 4], [5, -1, -3]])
m3 = mat([[2, 8, 3], [-1, 2, 2], [1, 4, 2]])
m4 = mat([[1, 2, 3], [2, 1, 2], [1, 3, 4]])
m5 = mat([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
m6 = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
m7 = mat([[1, 2, 5], [3, 7, 2], [4, 3, 1]])
print(m1 * m4.I)