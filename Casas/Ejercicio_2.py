
import pandas as pd



def p(variable):
    print(variable)

df=pd.read_csv('housing.csv')
pd.set_option('display.max_Columns', None)
df['rooms_relation']=df['total_rooms']/df['total_bedrooms']

dummies=pd.get_dummies(df['ocean_proximity'],dtype=int)

df=pd.concat([df,dummies],axis=1)
df.drop('ocean_proximity', axis=1, inplace=True)
df=df.dropna()
p(df.isna().sum())

p(df.head())

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

X=df.drop('median_house_value', axis=1)
y=df['median_house_value']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

for i in range(1,21):
    model = DecisionTreeRegressor(max_depth=i)
    model.fit(X_train, y_train)
    predicciones = model.predict(X_test)
    p(f" Max Depth de : {i}")
    p('Predicciones')

    p(predicciones)
    p('Score test')
    p(model.score(X_test, y_test))
    p('Score Train')
    p(model.score(X_train, y_train))
    p(' ')


model = DecisionTreeRegressor(max_depth=5)
model.fit(X_train, y_train)
predicciones = model.predict(X_test)
p(model.score(X_test, y_test))
p(model.score(X_train, y_train))

from sklearn.tree import plot_tree
from matplotlib import pyplot as plt

plt.figure(figsize=(100,80))
plot_tree(
    model,
    feature_names=X_train.columns,
    filled=True,
)
plt.show()

#Ingeniero, le dejo un for con depths de 1 al 20 ya para que vea como va cambiando
#los scores, los mejores resultados me han sido en el depth de 10 a 13 mas o menos,
#si lo subo mucho los datos train hacen que el score tenga 0.999, pero los test
#quedan en 0.65 mas o menos, le dejo un max depth de 5 para que se pueda apreciar el arbol
#asi lo hago desde pycharm, uno con mas depth como 20 tarda mucho o hasta
#advertencia de cargar la imagen en un lugar externo por el tamaño