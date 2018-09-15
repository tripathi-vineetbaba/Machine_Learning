import sys,time
sys.path.insert(0,'../../../Machine_Learning/')
from functions.sklearn_algorithms.sklearn_algorithms import Sklearn_Algorithm
from sklearn import model_selection

file_path='../../../Machine_Learning/data/naval_mine_identifier/naval_mine_identifier.all-data'

algos=Sklearn_Algorithm()
pd=algos.pd()
np=algos.np()

df=pd.read_csv(file_path)
df=df.values

X=df[:,:-1]
Y=df[:,-1]

print('*****************************************************************************************************')

#b'../../../../New_folder/testfile.csv'
#all_result=algos.get_accurqacy_all_algorithm(X,Y)
#print("\n\tAccuracy of algorithm on given IRIS data is as below :\n{0}".format(all_result))
#fit_algorithm=algos.get_fit_algorithm(X,Y)
#print("\n\tAlgorithm that suites most with this type of data :\n{0}".format(fit_algorithm))

algorithm,accuracy=algos.apply_fit_algorithm(X,Y)
print("\n\tAlgorithm applied on this data is {1}% accurate. Algorithm is : \t{0} ".format(algorithm,(accuracy*100)))
testfile=input("\n\tEnter file name with file location : ")
read_file=pd.read_csv(testfile,sep=',')
read_file=read_file.values
testY=read_file[:,-1]
testX=read_file[:,:-1]

trainX,test_X,trainY,test_Y=model_selection.train_test_split(X,Y,test_size=0.2,random_state=np.random.randint(len(X)))
algorithm.fit(trainX,trainY)

prediction=algorithm.predict(testX)
print('\n***********************************************PREDICTION AND ACTUAL VALUE************************************************\n')
for x in range(len(prediction)):
    print("Predicted Class : {0}\t\t\t {2} : {1}".format(prediction[x],testY[x],'Actual Class'))
#    else:
#        print("Predicted Class : {0}\t\t {2} : {1}".format(prediction[x],testY[x],'Actual Class'))
print("\n*************************************************ACCURACY****************************************\nOverall Accuracy : {0}".format(accuracy))

time.sleep(30)