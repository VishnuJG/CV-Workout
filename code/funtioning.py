import pandas as pd


data=pd.read_csv("datasetoutput.csv")
temp=list()
temp.append(0)
print(data.shape)
for i in range(1,data.shape[0]):
    temp.append(1)
data['target']=temp
print(data)
data.to_csv("D:\PES6\Capstone\Tests\datasetoutput.csv")