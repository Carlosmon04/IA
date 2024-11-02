import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
def p(v):
    print(v)

#Ahora con edades
df1=pd.read_csv('Altura_Con_Peso.csv')

df1.drop('Nombre',axis=1,inplace=True)

X1=df1.drop('Peso_(kg)',axis=1)
y1=df1['Peso_(kg)']

X1_train,X1_test,y1_train,y1_test=train_test_split(X1,y1,test_size=0.2)
model1=LinearRegression()
model1.fit(X1_train,y1_train)
predicciones1=model1.predict(X1_test)

p('Predicciones con X1_test')
p(predicciones1)
p(' ')

p('Predicciones con valores como 1.73 y 20 de Edad')
p(model1.predict([[1.73,20]]))
p(' ')

p('Scores')
p(model1.score(X1_train,y1_train))
print(model1.score(X1_test,y1_test))
p(' ')

p('porcentaje de error')
mse1=mean_squared_error(y1_test,predicciones1)
mse1=np.sqrt(mse1)
p(mse1)

