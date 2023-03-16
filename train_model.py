import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib

#Load data
import numpy as np

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = pd.DataFrame(raw_df.values[1::2, 2], columns=["MEDV"])
columns = [
            "CRIM",      
            "ZN",       
            "INDUS",    
            "CHAS",      
            "NOX",        
            "RM",       
            "AGE",     
            "DIS",      
            "RAD",      
            "TAX",       
            "PTRATIO",  
            "B",        
            "LSTAT"
            ]   
                     
df = pd.DataFrame(data, columns = columns)
# print(df.head())
# exit()
#boston = datasets.load_boston()
#df = pd.DataFrame(boston.data, columns = boston.feature_names)
#df['MEDV'] = boston.target 

#Split Model
X = df.copy() 
y = target.copy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 42)

#Model Creation
lm = LinearRegression()
lm.fit(X_train,y_train)


with open('model.joblib', 'wb') as f:
    joblib.dump(lm,f)


with open('model.joblib', 'rb') as f:
    predictor = joblib.load(f)

print("Testing following input: ")
print(X_test[0:1])
sampInput = pd.DataFrame([[0.09178, 0.0, 4.05, 0.0, 0.51, 6.416, 84.1, 2.6463, 5.0, 296.0, 16.6, 395.5, 9.04]], columns=columns)
#print(type(sampInput))
print(predictor.predict(sampInput))