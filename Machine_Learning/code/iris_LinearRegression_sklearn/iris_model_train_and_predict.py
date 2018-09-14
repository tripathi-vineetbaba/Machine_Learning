import sys,time
sys.path.insert(0,'../../../Machine_Learning/')
from functions.sklearn_algorithms.sklearn_algorithms import Sklearn_Algorithm
from data.iris.iris import IrisData as iris
from sklearn import model_selection
algos=Sklearn_Algorithm()
pd=algos.pd()
np=algos.np()
url=iris.urls()
column=iris.columns()
df=pd.read_csv(url,sep=',',names=column)
df=df.values
X=df[:,:-1]
Y=df[:,-1]
print('*****************************************************************************************************')

#all_result=algos.get_accurqacy_all_algorithm(X,Y)
#print("\n\tAccuracy of algorithm on given IRIS data is as below :\n{0}".format(all_result))
#fit_algorithm=algos.get_fit_algorithm(X,Y)
#print("\n\tAlgorithm that suites most with this type of data :\n{0}".format(fit_algorithm))
algorithm,accuracy=algos.apply_fit_algorithm(X,Y)
print("\n\tAlgorithm that is applied : \n{0}".format(algorithm))
trainX,testX,trainY,testY=model_selection.train_test_split(X,Y,test_size=0.2,random_state=np.random.randint(len(X)))
algorithm.fit(trainX,trainY)
prediction=algorithm.predict(testX)
print('*****************************************************************************************************')
for x in range(len(prediction)):
    if testY[x]=='Iris-setosa':
        print("Predicted Class : {0}\t\t\t {2} : {1}".format(prediction[x],testY[x],'Actual Class'))
    else:
        print("Predicted Class : {0}\t\t {2} : {1}".format(prediction[x],testY[x],'Actual Class'))
print("*****************************************************************************************************\nOverall Accuracy : {0}".format(accuracy))

time.sleep(30)