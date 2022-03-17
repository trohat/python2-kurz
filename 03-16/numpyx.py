import numpy as np

pole1 = np.array([5,8,9,15,26])
pole2 = np.arange(2, 30, 2)

pole3 = np.linspace(1, 10, 10)

pole4 = np.zeros((3,7))

pole5 = np.ones((4,5))

print(pole1.max())

print(pole2.min())

print(pole3)
print(pole3.sum())

nove_pole = pole4 + 15

jeste_nove_pole = pole5.reshape((2, 10))

# http://jalammar.github.io/visual-numpy/
# https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d

