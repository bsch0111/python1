
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings('ignore')

data=pd.read_csv('C:/train.csv')
data.head()
data.isnull().sum()

data['Survived'].value_counts()
data['Pclass'].value_counts()
data['Pclass'].count()

f,ax = plt.subplots(1,2,figsize=(18,8))
data['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0])
sns.countplot('Pclass',data=data,ax=ax[1])
#plt.show()

data.isnull().sum()
data['Embarked'].value_counts().plot.pie()
#plt.show()

data.groupby(['Sex','Survived']).count()
data.groupby(['Sex','Survived'])['Survived'].count()
data.groupby(['Sex','Survived']).size()

data[['Sex','Survived']].groupby('Sex').count()

f,ax = plt.subplots(1,2,figsize=(18,8))
data[['Sex','Survived']].groupby('Sex').mean().plot.bar(ax=ax[0])
ax[0].set_title("Survived vs Sex")
sns.countplot('Survived',hue='Sex',data=data,ax=ax[1])
ax[1].set_title("Sex::Survived vs Dead")
#plt.show()

ob = pd.crosstab(data.Survived,data.Sex,margins=True,normalize = True).style.background_gradient(cmap='summer_r')

sns.countplot('Pclass',data=data,ax=ax[0])
sns.countplot('Pclass',hue='Survived',data=data, ax=ax[1])
plt.show()

data['Pclass'].value_counts().plot.pie(autopct='%1.1f%%',ax=ax[0])
data['Pclass'].value_counts().plot.bar(color=['red','red','red'],ax=ax[0])

pd.crosstab([data.Sex,data.Survived],[data.Pclass],margins=True)
sns.factorplot('Pclass','Survived',hue='Sex',data=data,ax=ax[1])
plt.show()

data['Age'].max()
data['Age'].min()
data['Age'].mean()
data['Age'].median()


sns.violinplot('Pclass','Age',hue='Survived',split=True,data=data,ax=ax[1])
ax[1]=set_title('Pclass and Age vs Survived')
ax[1]=set_yticks(range(0,110,10))
plt.show()

data.isnull().sum()

data['Initial'] = 0 


data['Survived'].isin(['1'])
data.Name.head()

data['Start'] = 0
data['End'] = 0

data['Start'] = data['Name'].str.find('Mr')[data['Name'].str.find(sub='Mr') > 0]

data['Initial'] = data['Name'].str.strip()
data[["Start","End"]] = data['Name'].str.split(',',expand=True)
data[["Name","End","Start"]] = data['End'].str.split('.',expand=True)
data['End'].str.split('.',expand=True)

data[["Name","End","Start"]]

data['Name'] = data['Name'].str.strip()
data['Name'].replace(['Mlle','Mme','Ms','Dr','Major','Lady','Countess','Jonkheer','Col','Rev','Capt','Sir','Don'],['Miss','Miss','Miss','Mr','Mr','Mrs','Mrs','Other','Other','Other','Mr','Mr','Mr'],inplace=True)
data.isnull().sum()
data.groupby('Name').mean()


data['Name']
data['Start']
data['End']

data.isnull().sum()

data[(data.Age.isnull())&(data.Name=='Mr')]['Age']
data.loc[(data.Age.isnull())&(data.Name=='Mr'),'Age']

data[(data.Age.isnull())&(data.Name=='Mr')]['Age']=33
data[(data.Age.isnull())&(data.Name=='Mrs')]['Age']=36
data[(data.Age.isnull())&(data.Name=='Master')]['Age']=5
data[(data.Age.isnull())&(data.Name=='Miss')]['Age']=22
data[(data.Age.isnull())&(data.Name=='Other')]['Age']=46

data.loc[(data.Age.isnull())&(data.Name=='Mr'),'Age']=33
data.loc[(data.Age.isnull())&(data.Name=='Mrs'),'Age']=36
data.loc[(data.Age.isnull())&(data.Name=='Master'),'Age']=5
data.loc[(data.Age.isnull())&(data.Name=='Miss'),'Age']=22
data.loc[(data.Age.isnull())&(data.Name=='Other'),'Age']=46