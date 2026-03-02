# importing the required module
import matplotlib.pyplot as plt
import random

x = [1, 2, 3, 4, 5, 6]
y = [0, 0, 0, 0, 0, 0]
for i in range(100000):
    throw = random.randint(1,6)
    y[throw-1] +=1

plt.plot(x, y)

plt.xlabel('Number')
plt.ylabel('Frequency')

plt.title('My first graph!')

plt.show()