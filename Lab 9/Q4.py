import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Student_age.csv")

ages=["15-28","29-40"]
A1=df[(df['Age']>15)&(df['Age']<=28)].shape[0]
A2=df[(df['Age']>28)&(df['Age']<=40)].shape[0]

Age=[A1,A2]
plt.pie(Age,labels=ages)
plt.title("Student Age Distribution")
plt.show()
