import numpy as np
import matplotlib.pyplot as plt

def y(n, a):
    return (1 - (-a)**(n+1)) / (1 + a)

# Define the range of n values
n_values = np.arange(0, 10)

# Define the value of a
a = 0.5

# Calculate y values
y_values = y(n_values, a)

# Plotting as discrete sequence
plt.stem(n_values, y_values)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid(True)
plt.show()
