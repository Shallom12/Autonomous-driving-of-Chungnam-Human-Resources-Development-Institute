import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\user\Documents\카카오톡 받은 파일\04_data2.csv")

PetalLength = data['PetalLength']
Petalwidth = data['PetalWidth']
plt.figure(figsize= (10,4))
plt.scatter(PetalLength, Petalwidth)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Iris Petal Scatter Graph')
plt.grid()
plt.show() 
