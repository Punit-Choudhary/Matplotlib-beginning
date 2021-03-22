import matplotlib.pyplot as plt
# We started with importing matplotlib's pyplot module as an alias plt.

number_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # List containing data
plt.plot(number_values, squares, linewidth=5) # plot() function plots a graph using passed data

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

# Set the size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show() # show() function renders graph
