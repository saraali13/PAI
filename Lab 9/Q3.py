import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Cheese Strawberry', 'Butter Scotch']
sales = [150, 60, 80, 200, 85]

plt.pie(sales, labels=flavors)
plt.title('Ice Cream Sales Distribution')
plt.show()
