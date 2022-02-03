#!pip install pandas
#!pip install seaborn

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import cv2


df = pd.read_csv("F:/Image Processing using python/data.csv")
print(df.describe())
print(df.describe().T)

# Find the null values in dataset

print(df.isnull().sum())

# rename a column dataset for better understanding

df = df.rename(columns = {'diagnosis': 'Label'})
print(df.dtypes)

# Replace categories values with numbers

df['Label'].value_counts()
categories = {'B': 1, 'M': 2}
df['Label'] = df['Label'].replace(categories)

# define the dependent variable that need to be predicted (Label= {'B': 1, 'M': 2})

Y = df['Label'].values   #.values gives Array of int64
#Y1 = df['Label']  # Series

# droping 2 columns id and Label, which are not used as independent variables.

X = df.drop(labels = ['Label', 'id','Unnamed: 32'], axis=1)

# Split data into train and test

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state= 42)

# Now apply machine learning Algorithm (support vector machine = SVM)

from sklearn import svm

model = svm.LinearSVC(max_iter = 10000)

#model = SVC(kernel='linear', C=10, gamma=1000, max_iter=10000)

model.fit(X_train, Y_train)

# now prediction

prediction = model.predict(X_test)

from sklearn import metrics
print ("Accuracy = ", metrics.accuracy_score(Y_test, prediction))

#Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, prediction)
print(cm)

#Print individual accuracy values for each class, based on the confusion matrix
print("With Lung disease = ", cm[0,0] / (cm[0,0]+cm[1,0]))
print("No disease = ",   cm[1,1] / (cm[0,1]+cm[1,1]))


#  Normalising data for better accuracy

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import QuantileTransformer

scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)

















