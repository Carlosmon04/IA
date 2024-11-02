import pandas as pd

def p(variable):
    print(variable)


df=pd.read_csv('Alturas.csv')

df.drop('Nombre',axis=1,inplace=True)
p(df)
p(df.isna().sum())
X=df.drop('Peso_(kg)',axis=1)
y=df['Peso_(kg)']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
# p(X_test)
model=LinearRegression()
model.fit(X_train,y_train)
predicciones=model.predict(X_test)
p('Predicciones con X_test')
p(predicciones)
p('Predicciones con  un valor por ejemplo altura 1.73')
p(model.predict([[1.70]]))
p(' ')
p('scores con train y test')
print(model.score(X_train,y_train))
print(model.score(X_test,y_test))
p(' ')

from sklearn.metrics import mean_squared_error
import numpy as np
p('Porcentaje de error')
mse= mean_squared_error(y_test,predicciones)
mse=np.sqrt(mse)
p(mse)


