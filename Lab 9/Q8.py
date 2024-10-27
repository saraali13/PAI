import matplotlib.pyplot as plt

x = [1,2,3,4,5]  # X-axis values
y1 = [12,15,18,20,25]  # Data for y1
y2 = [7,8,10,13,21]  # Data for y2

plt.plot(x, y1, 'o-', color='pink', label='y1 Data')
plt.plot(x, y2, 'o-', color='gray', label='y2 Data')

plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(loc='lower right')
plt.show()
