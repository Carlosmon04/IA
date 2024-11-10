import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def p(variable):
    print(variable)

pd.set_option('display.max_columns', None)
df=pd.read_csv('housing.csv')

df['Rooms_Totals']= df['total_rooms']/df['total_bedrooms']
p(df['Rooms_Totals'].mean()) #veo promedio de Cuartos
df['Rooms_Totals']=df['Rooms_Totals'].fillna(df['Rooms_Totals'].mean())



dummiesOcean=pd.get_dummies(df['ocean_proximity'],dtype=int)
df=pd.concat([df,dummiesOcean],axis=1)
df.drop('ocean_proximity', axis=1, inplace=True)

df = df[df['housing_median_age'] <= 50]


df['Precios_Categoria'] = pd.cut(
    df['median_house_value'],
    bins=[0, 250000, 500000],
    labels=[0, 1]
)


p(df.head)


df.dropna(inplace=True)
df.drop(['total_rooms','total_bedrooms'],axis=1,inplace=True)


X=df.drop('median_house_value', axis=1)
y=df['median_house_value']
p('casas')
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)


predicciones=model.predict(X_test)

comparativa={
      'Preidcciones':predicciones,
      'Valor Real':y_test
  }
resultado=pd.DataFrame(comparativa)
p('Comparacion')
p(resultado)

s=model.score(X_test,y_test)
sa=model.score(X_train,y_train)
p('scores')
p(sa)
p(s)



df.hist(bins=50, figsize=(20,15), edgecolor='black')
# plt.show()
# plt.figure(figsize=(8,6))
# sb.heatmap(df.corr(),annot=True)
# plt.show()
#
#

