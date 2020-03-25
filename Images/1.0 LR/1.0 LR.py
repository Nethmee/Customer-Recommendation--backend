no_ptcpnt=eval(input('ENter the no of participant'))
import cv2
import numpy as np
import pandas as pd 
#feature-weight,label-height
#creating a numpy array with zeros
data=np.zeros((1,no_ptcpnt),np.intc)#parameters :shape of the array (row,column),data type
target=np.zeros((1,no_ptcpnt),np.intc)
print(target)
for i in range(no_ptcpnt):
    weight=eval(input('Partcipant '+str(i+1)+'Enter your weight(in kg):'))
    data[0,i]=weight
    height=eval(input('Partcipant '+str(i+1)+'Enter your height(in cm):'))
    target[0,i]=height
  


#pd.DataFrame(data).to_csv("C:\Users\user\Desktop\Machine-Learning\Week-05-Group4-master\Codes/file.csv")
#data2=np.zeros(1,no_ptcpnt)#this should be written as data2=np.zeros([1,no_ptcpnt])
np.savetxt("testData.csv",data, delimiter=",")
print(data)
print(target)

import pickle

pickle.dump(data,open('data.pickle','wb'))
pickle.dump(target,open('target.pickle','wb'))




