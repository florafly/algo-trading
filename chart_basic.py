import matplotlib.pyplot as plt

# prices of financial assets
prices = [100, 120, 80, 140, 90]

# create a list of labels for the x-axis
labels = ['Asset A', 'Asset B', 'Asset C', 'Asset D', 'Asset E']

# create a bar chart
plt.bar(labels, prices)

# add a title to the chart
plt.title('Financial Asset Prices')

# add labels to the x and y axes
plt.xlabel('Assets')
plt.ylabel('Price')

# display the chart
plt.show()