import os
import pandas as pd
import numpy as np
import pickle
os.chdir(os.path.join(__file__,os.path.pardir))

# data=pd.read_csv('data_guest.csv',index_col=0)
# print(data.head())
# x=data[['imei','mac','cpucore']].values
# y=np.zeros(len(x))
# output_data={'X':x,'y':y}

# output = open('data.pkl', 'wb')

# pickle.dump(output_data, output)
columns=[]
for i in range(0,79):
    columns.append('{}'.format(i))

# data=np.random.randn(75,79)
# data=pd.DataFrame(data,columns=columns)
# #print(data)
# y=np.zeros((len(data),1))

# output_data={'X':data,'y':y}

# output = open('data.pkl', 'wb')

# pickle.dump(output_data, output)

for i in range(5):
    data=np.random.randn(75,79)
    data=pd.DataFrame(data,columns=columns)
    data['y']=np.zeros((len(data),1))
    for j in range(np.random.randint(0,50)):
        data['y'][np.random.randint(0,74)]=1
    data.to_csv('{}.csv'.format(i),index=False)