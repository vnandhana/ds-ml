from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrices
from sklearn import svm
cancer=datasets.load_breast_cancer()
x_train,x_test,y_train,y_test=train_test_split(cancer.data,cancer.target,test_size=0.3,random_state=109)
clf=svm.SVC(kernel='linear')
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
print("Actual values",y_test)
print("Predicted values",y_pred)
print("Accuracy:",metrices.accuracy_score(y_test,y_pred))
print("Precision:",metrices.precision_score(y_test,y_pred))
print("Recall:",metrices.recall_score(y_test,y_pred))