import matplotlib.pyplot as plt

cities = ['Karachi', 'Lahore', 'Islamabad', 'Hyderabad', 'Multan']
populations = [2500000, 1200000, 800000, 450000, 750000]

plt.barh(cities, populations, color='Blue')
plt.xlabel('Population')
plt.title('Population of Cities')
plt.show()
