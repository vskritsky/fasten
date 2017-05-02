#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:16:21 2017

@author: administrator
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import svm
import pandas as pd
import numpy as np

#classification task is done by space vector machine
train_data = pd.read_csv('classification_train.csv', delimiter=',')
#some of provided data are corrupted - contain NaN
train_data = train_data.fillna(value='0')
#separate features from result
X = train_data.iloc[:,1:25]
y = train_data.iloc[:,25:26]
#based on features fit with space vector classificator
clf = svm.SVC()
clf.fit(X, y.values.ravel())

#check classification on test data
test_data = pd.read_csv('classification_test.csv', delimiter=',')
test_data = test_data.fillna(value='0')
X_ = test_data.iloc[:,1:25]
df = clf.predict(X_)
#saving results to a .csv file
index = [int(i) for i in range(1, len(df)+1)]
df = pd.DataFrame(data=df, index=index)
print(df)
np.savetxt('sample_submission.csv', df.astype(int), fmt='%i', delimiter=",")
