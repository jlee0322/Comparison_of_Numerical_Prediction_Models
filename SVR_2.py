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
    acc = pd.read_csv('accelerometer.data')
    
    #get train data
    x = acc.iloc[:,[2,3,4]]
    y = acc.iloc[:,0]

    x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.3 ,random_state = 0)
    
    #std
    x_std = StandardScaler()
    x_std_train = x_std.fit_transform(x_train)
    x_std_test = x_std.transform(x_test)
    
    #fit
    SVR = svm.SVR(kernel = 'rbf')
    SVR.fit(x_std_train,y_train.astype('int'))
    
    #predict
    y_pred_test = SVR.predict(x_std_test)
    
    #score
    print('MAE: ', mean_absolute_error(y_test, y_pred_test))
    print('RMSE: ', mean_squared_error(y_test, y_pred_test, squared=False))
    print('MAPE: ', mean_absolute_percentage_error(y_test, y_pred_test))
    
if __name__ == '__main__':
    main()
