import os,sys

sys.path.insert(0,'../../../Machine_Learning/')
from functions.regression.regression import Regression as regression
from connections.database.code.sqllite_connection_manager import DatabaseConnection as connect
from functions.OS.OS import OS
from data.iris.iris import IrisData as iris
import tensorflow as tf
import pandas as pd
import numpy as np
from functions.costs.costs import Cost

url=iris.urls()
column=iris.columns()
df=pd.read_csv(url,sep=',',names=column)


Len_Pet=df.values[:,2]
Wid_Pet=df.values[:,3]
ClassName=df.values[:,4]
Len_Sep=df.values[:,0]
Wid_Sep=df.values[:,1]


train_Lenpet=Len_Pet[0:150].reshape(-1,1)
test_Lenpet=Len_Pet[150:-1].reshape(-1,1)
test_Widpet=Wid_Pet[150:-1].reshape(-1,1)
train_Widpet=Wid_Pet[0:150].reshape(-1,1)

learning_rate=0.01
epochs=100
display_steps=50

train_Lensep=Len_Sep[0:150].reshape(-1,1)
test_Lensep=Len_Sep[150:-1].reshape(-1,1)
test_Widsep=Wid_Sep[150:-1].reshape(-1,1)
train_Widsep=Wid_Sep[0:150].reshape(-1,1)

W=tf.Variable(np.random.randn(),name='Weight')
B=tf.Variable(np.random.randn(),name='Bias')
sample=train_Lenpet.shape[0]
init=tf.global_variables_initializer()



X=tf.placeholder("float")
Y=tf.placeholder("float")


#regression.LinearRegression(Data,Weight,Bias)
pred=regression.LinearRegression(X,W,B)

#Cost.RMSE(prediction,actual,number_of_sample)
cost=Cost.RMSE(pred,Y,sample)

optimizer=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

model=OS.createDirectory(self=OS,filename='irisData')
model_Pet=model+'Pet'
model_Sep=model+'Sep'

saver=tf.train.Saver()

save_path=''

#regression.computeRegression(sess,epochs,X_axis_Data,Y_axis_Data,optimizer,display_steps,X-placeholder,Y-placeholder,cost,weight,bias,model,global_steps)
with tf.Session() as sess:
    sess.run(init)
    storePet,savePet=regression.computeRegression(regression,sess,epochs,Wid_Pet,Len_Pet,optimizer,display_steps,X,Y,cost,W,B,model_Pet) #Linear Regression for petal width & length
    storeSep,saveSep=regression.computeRegression(regression,sess,epochs,Wid_Sep,Len_Sep,optimizer,display_steps,X,Y,cost,W,B,model_Sep) #Linear regression for sepal width & length
    print("Petal Details")
    c=storePet[-1][1]
    w=storePet[-1][2]
    b=storePet[-1][3]
    print("Cost : ","{:.9f}".format(c)," Weight : ",w," Bias : ",b)
    print("Model file is saved at : ",savePet)
    #for epoch,c,w,b in storePet[-1]:
    #    print("Epoch : ",'%04d' %(epoch+1)," cost : ","{:.9f}".format(c)," Weight : ",w," Bias : ",b)
    print()
    print("Sepal Details")
    c=storeSep[-1][1]
    w=storeSep[-1][2]
    b=storeSep[-1][3]
    print("Cost : ","{:.9f}".format(c)," Weight : ",w," Bias : ",b)
    print("Model file is saved at : ",saveSep)
    #for epoch,c,w,b in storeSep[-1]:
    #    print("Epoch : ",'%04d' %(epoch+1)," cost : ","{:.9f}".format(c)," Weight : ",w," Bias : ",b)

print()
print("Optimization Completed.")



