#The best way to represent data
# in Scikit-learn is in the form of tables. A table represents a 2-D grid of data where rows represent the individual 
# elements of the dataset the columns represents the quantities related to those individual elements.
import sys
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
sns.set()
sns.pairplot(iris, hue="species", height=3)
X_iris = iris.drop("species", axis=1)
print(X_iris.shape)
y_iris = iris["species"]
print(y_iris.shape)
plt.show()
