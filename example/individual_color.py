import matplotlib.pyplot as plt
from bg_mpl_stylesheets.colors import Colors

# Example data
x = [0, 1, 2, 3, 4, 5]
y = [i ** 2 for i in x]  # Example data: y = x^2

# Plotting with enum color
bg_blue_hex = Colors.bg_blue.value
bg_blue_name = Colors.bg_blue.name

plt.plot(x, y, color=bg_blue_hex, label=f'Color: {bg_blue_name}')  # Using the enum value for color
plt.title("Plot Example Using Enum Colors")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()