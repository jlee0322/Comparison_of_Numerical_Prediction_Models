from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sklearn.preprocessing as sp
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error


def main():
    #load dataset
    adult = pd.read_csv('adult.data')
    adult_test = pd.read_csv('adult.test')
    
    #get train data
    x_train = adult.iloc[:,[0,2]].values
    y_train = adult['hours-per-week'].values

    #get test data
    x_test = adult_test.iloc[:,[0,2]].values
    y_test = adult_test['hours-per-week'].values
    print(x_test)

    #Encoder
    label = sp.LabelEncoder()
    x_train[:,1] = label.fit_transform(x_train[:,1])
    x_test[:,1] = label.fit_transform(x_test[:,1])
    
    #std
    x_std = StandardScaler()
    x_std_train = x_std.fit_transform(x_train)
    x_std_test = x_std.transform(x_test)
    
    #print(y_train)
    #print(y_test)
    
    #fit
    linearModel = svm.SVR(kernel = "rbf")
    linearModel.fit(x_std_train,y_train)
    
    #predict
    y_pred_test = linearModel.predict(x_std_test)
    
    #score
    print('MAE: ', mean_absolute_error(y_test, y_pred_test))
    print('RMSE: ', mean_squared_error(y_test, y_pred_test, squared=False))
    print('MAPE: ', mean_absolute_percentage_error(y_test, y_pred_test))
    
    

if __name__ == '__main__':
    main()
