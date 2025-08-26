import numpy
import pandas as pd
import matplotlib.pyplot  as plt
 


hours = [2, 3 , 5 , 7 , 9 , 10 , 11 , 12]
score = [50, 55 , 65 , 75 , 85, 90, 95, 100]
# combined = arr + arry
plt.plot(hours, score, marker='o', color='blue', linestyle='-', linewidth=2)

 
plt.title('Study Hours vs Score')
plt.xlabel('Hours of Study')
plt.ylabel('Score')

 
plt.grid(True)

 
plt.show()
# mean = sum(arr)/len(arr)
# df = pd.DataFrame({
#     'hours': hours,
#     'score': score
# })
# print(df)
# print("Mean :" , mean)


 