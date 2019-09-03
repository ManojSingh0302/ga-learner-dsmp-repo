# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df = pd.read_csv(path)
print(df.head())
print(df.info())

df[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']] = df[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']].replace('\$','',regex=True)
df[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']] = df[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']].replace('\,','',regex=True)
print(df.head())

X = df.drop(['CLAIM_FLAG'], 1).copy()
y = df['CLAIM_FLAG'].copy()

count = df['CLAIM_FLAG'].value_counts()
print('value count of CLAIM_FLAG', count)
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size = 0.3, random_state = 6)




# Code ends here


# --------------
# Code starts here
X_train[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']] = X_train[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']].astype(float)

X_test[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']] = X_test[['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']].astype(float)

print(X_train.isnull().values.any())
print(X_test.isnull().values.any())
# Code ends here


# --------------
# Code starts h
X_train = X_train.dropna(subset=['YOJ', 'OCCUPATION'])
X_test = X_test.dropna(subset=['YOJ', 'OCCUPATION'])

#Update the index of target
y_train = y_train[X_train.index]
y_test = y_test[X_test.index]

#Fill the missing values for columns  
X_train[['AGE','CAR_AGE','INCOME','HOME_VAL']].fillna(X_train[['AGE','CAR_AGE','INCOME','HOME_VAL']].mean(),inplace=True)
X_test[['AGE','CAR_AGE','INCOME','HOME_VAL']].fillna(X_test[['AGE','CAR_AGE','INCOME','HOME_VAL']].mean(),inplace=True)



# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
le = LabelEncoder()
for col in columns:
    try:
        X_train[col] = le.fit_transform(X_train[col].astype(str))
        X_test[col] = le.transform(X_test[col].astype(str))
    except:
        print('Error encoding '+ col)
# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# code starts here 
print(X_train.info())
X_train.fillna(X_train[['AGE','CAR_AGE','INCOME','HOME_VAL']].mean(),inplace=True)
X_test.fillna(X_test[['AGE','CAR_AGE','INCOME','HOME_VAL']].mean(),inplace=True)
print(X_train.info())
print(X_test.info())
model = LogisticRegression(random_state=6)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print('Accuracy Score {}', score)
precision = precision_score(y_test, y_pred)
print('Precision Score {}', precision)
# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
#Instantiate a SMOTE
smote = SMOTE(random_state=9)
X_train, y_train = smote.fit_sample(X_train, y_train)

#Instantiate a StandardScaler
scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)
# Code ends here


# --------------
# Code Starts here
model = LogisticRegression(random_state=6)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
score = accuracy_score(y_test, y_pred)
print('Accuracy Score {}', score)
# Code ends here


