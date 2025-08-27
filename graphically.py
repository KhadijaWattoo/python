import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[10,20,30,40,50]

# plt.plot(x,y)
# plt.scatter(x,y)
# plt.pie(x,y)
# plt.show()
# labels = ['A', 'B', 'C', 'D']
# sizes = [10, 20, 30, 40]
# colors = ['darkred', 'lightblue', 'pink', 'lightgreen']

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
# plt.title('Pie Chart')
# plt.show()
# data = [10, 20, 30, 40, 50, 10, 30, 45, 35, 25 , 55]

# plt.boxplot(data)
# plt.title('Box Plot')
# plt.show()
plt.step(x, y, color='m')
plt.title('Step Plot')
plt.show()
