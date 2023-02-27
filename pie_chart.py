import matplotlib.pyplot as plt

slices = [7,6,5,9]
activities = ['A','B','C','D']
cols = ['c','g', 'y', 'b']
explode = [0.1,0,0,0]
wedgedprops = {'edgecolor':'red', 'linewidth': 1, 'linestyle': '--', 'antialiased': True}
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow= True, explode=explode, autopct='%1.1f%%',
        pctdistance=0.5, labeldistance=1.1, wedgeprops=wedgedprops)
plt.title('Any details in Pie Plot')
plt.legend()
plt.show()
