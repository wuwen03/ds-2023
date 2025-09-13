import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
data=pd.read_csv("boston.csv")
print(data.keys())
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data.iloc[:,:-1],data['MEDV'],random_state=0)
lr=LinearRegression()
lr.fit(x_train,y_train)
LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None)
print(lr.coef_)