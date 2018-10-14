import numpy,pandas,random,os,time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import explained_variance_score
from sklearn import model_selection
os.system('cls')
class Sklearn_Algorithm:

    model=[]

    def __init__(self):
        self.model=[]



    def pd(self):
        return pandas

    def np(self):
        return numpy


    def get_model(self):
        #self.model.append(('LinearRegression',LinearRegression()))
        self.model.append(('GaussianNB',GaussianNB()))
        self.model.append(('LinearDiscriminantAnalysis',LinearDiscriminantAnalysis()))
        self.model.append(('KNeighborsClassifier',KNeighborsClassifier()))
        self.model.append(('DecisionTreeClassifier',DecisionTreeClassifier()))
        self.model.append(('SVC',SVC()))
        return self.model


    def get_accurqacy_all_algorithm(self,X,Y,all_algorithm=[]):
        trainX,testX,trainY,testY=model_selection.train_test_split(X,Y,test_size=0.2,random_state=numpy.random.randint(len(X)))
        modelList=self.get_model()
        for name,modelFunc in modelList:
            model=modelFunc
            model.fit(trainX,trainY)
            prediction=model.predict(testX)
            if name=='LinearRegression':
                accuracy=explained_variance_score(prediction,testY)
            else:
                accuracy=accuracy_score(prediction,testY)
            all_algorithm.append([name,accuracy])
        df=pandas.DataFrame(all_algorithm,columns=['Algorithm','Accuracy_of_Algorithm'],index=['','','','',''])
        return df

    def get_fit_algorithm(self,X,Y):
        dataset=self.get_accurqacy_all_algorithm(X,Y)
        max=dataset['Accuracy_of_Algorithm'].max()
        dataFrame=dataset[dataset['Accuracy_of_Algorithm']==max][['Algorithm','Accuracy_of_Algorithm']]
        return dataFrame

    def apply_fit_algorithm(self,X,Y):
        dataFrame=self.get_fit_algorithm(X,Y)
        model=self.get_model()
        x=random.choice(dataFrame.loc[:,'Algorithm'].values)
        y=random.choice(dataFrame.loc[:,'Accuracy_of_Algorithm'].values)
        for k in range(len(model)):
            if x==model[k][0]:
                return model[k][1],y