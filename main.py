import random
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statistics
import time

# Total number of stickers in the album
total_stickers = 670

# Price of the stickers package
package_price = 4

# Number of stickers per package
sticker_per_package = 5

# Number of iterations you would like to run
number_of_iterations = 50


def monte_carlo(total_stickers, package_price, sticker_per_package, number_of_iterations):
    # List storing the total price of all iterations
    price = []

    # Loop with the number of operations
    for iteration in range(number_of_iterations):

        # List representing our album
        album = []

        # Counter of sticker used to complete the album
        stickers_count = 0

        while len(album) < total_stickers:

            # Count the sticker we using
            stickers_count += 1

            # Randomly selects a number representing our sticker
            sticker = random.randint(1, total_stickers)

            # Verify if our sticker is already in our album
            if sticker not in album:
                album.append(sticker)

        # Calculate the number of packages needed to reach the stickers_count amount of stickers
        total_packages = stickers_count // sticker_per_package + 1

        # Calculate the total price for this simulation
        total_price = total_packages * package_price

        # Append the total price to the list price
        price.append(total_price)

    return price


# Initial time of the function
start = time.time()

# Do the Monte Carlo simulation and gets the vector with the data 
data = monte_carlo(total_stickers, package_price, sticker_per_package, number_of_iterations)

# Final time of the function
end = time.time()

# Total time spent
time_spent = end - start

# Create the histogram
histogram = sns.histplot(data)

# Set histogram X axe name
histogram.set_xlabel(xlabel="Price ($)")

# Plot the histogram
plt.show()

# Create the boxplot
boxplot = sns.boxplot(x=data)

# Plot the boxplot
plt.show()

# Calculate the mean, standard deviation, median, 1st quartile, 3rd quartile and IQR
mean = round(statistics.mean(data), 2)
standard_deviation = round(statistics.pstdev(data), 2)
median = round(statistics.median(data), 2)
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
iqr = round(q3 - q1, 2)

# Print the statistics and time information calculated before
print("----------- Statistical Parameters -----------")
print(f"mean:\t{mean}\nstandard deviation:\t{standard_deviation}")
print(f"median:\t{median}\nInterquartile range:\t{iqr}")
print("--------------- Time Parameters --------------")
print(f"time spent:\t{time_spent}\nnumber od iterations:\t{number_of_iterations}")
