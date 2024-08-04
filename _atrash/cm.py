# first we importing the necessary things like sklearn pandas etc
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import model_selection
#creating the variable crop and storing the csv file in it that contain the data of the diffent crops
# that was taken from diffrent websites from internet
crop = pd.read_csv('Data/crop_recommendation.csv')
X = crop.iloc[:,:-1].values
Y = crop.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.15)
#creating a list that has ourmodel as a list
ourmodle = []
ourmodle.append(('SVC', SVC(gamma ='auto', probability = True)))
ourmodle.append(('svm1', SVC(probability=True, kernel='poly', degree=1)))
ourmodle.append(('svm2', SVC(probability=True, kernel='poly', degree=2)))
ourmodle.append(('svm3', SVC(probability=True, kernel='poly', degree=3)))
ourmodle.append(('svm4', SVC(probability=True, kernel='poly', degree=4)))
ourmodle.append(('svm5', SVC(probability=True, kernel='poly', degree=5)))
ourmodle.append(('rf',RandomForestClassifier(n_estimators = 21)))
ourmodle.append(('gnb',GaussianNB()))
ourmodle.append(('knn1', KNeighborsClassifier(n_neighbors=1)))
ourmodle.append(('knn3', KNeighborsClassifier(n_neighbors=3)))
ourmodle.append(('knn5', KNeighborsClassifier(n_neighbors=5)))
ourmodle.append(('knn7', KNeighborsClassifier(n_neighbors=7)))
ourmodle.append(('knn9', KNeighborsClassifier(n_neighbors=9)))

vot_soft = VotingClassifier(estimators=ourmodle, voting='soft')
vot_soft.fit(X_train, y_train)
y_pred = vot_soft.predict(X_test)
#after testing after traing we can check our accuracy of teh model which is amazing in thsi case
scores = model_selection.cross_val_score(vot_soft, X_test, y_test,cv=5,scoring='accuracy')
print("Accuracy: ",scores.mean())

score = accuracy_score(y_test, y_pred)
print("Voting Score % d" % score)

import pickle
filepklname = 'crop_recommendation.pkl'
pklmodleel = open(filepklname, 'wb')
pickle.dump(vot_soft, pklmodleel)
pklmodleel.close()