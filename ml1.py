from sklearn.datasets import load_iris
import time
print("Loading: |", end="")
for i in range(10):
    print("\rLoading:", "#"*(i+1), "-"*(10-i-1), "|", end="")
    time.sleep(0.5)
iris=load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.3,random_state=1
)
#Train themodel part 1
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
classifier_knn= KNeighborsClassifier(n_neighbors=3)
classifier_knn.fit(x_train,y_train)
y_pred=classifier_knn.predict(x_test)
print("accuracy",metrics.accuracy_score(y_test,y_pred))
sample=[[5,5,3,2],[3,4,5,3]]
preds=classifier_knn.predict(sample)
pred_species=[iris.target_names[p] for p in preds]
print("predictions:",pred_species)

