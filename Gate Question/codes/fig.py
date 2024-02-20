import numpy as np
import matplotlib.pyplot as plt

# Define the function
def y_n(n, a):
    return (1 - (-a)**n) / (1 - (-a))

# Generate values for n
n_values = np.arange(0, 10, 1)  # Adjust the range and step size as needed

# Choose a value for 'a'
a = 0.5  # You can change this value as needed

# Calculate corresponding y values
y_values = y_n(n_values, a)

# Plot the function
plt.plot(n_values, y_values, marker='o')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Plot of y(n)')
plt.grid(True)
plt.show()