# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here

df = pd.read_csv(path)
print (df.head(1))

#feature_cols =['ages','num_reviews','piece_count','play_star_rating','review_difficulty',         'star_rating', 'theme_name','val_star_rating']
#X = df.loc[:, feature_cols]
X=df[['ages','num_reviews','piece_count','play_star_rating','review_difficulty',         'star_rating', 'theme_name','val_star_rating', 'country']]
print (X.head(1))
print (X.shape)
y= df['list_price']
#print (y.head(1))
print (y.shape)
#Split the dataframe

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols = X_train.columns
print (cols)

fig, axes = plt.subplots(nrows = 3 , ncols = 3, sharex='col', sharey='row')

for i in range(3):
    for j in range (3):
        col=cols[ i * 3 + j]
        axes[i,j].scatter(X_train[col],y_train)


# code ends here



# --------------
# Code starts here
import seaborn as sns
corr=X_train.corr()
sns.heatmap(corr, annot=True, cmap=plt.cm.Reds)
plt.show()
#Using Pearson Correlation

X_train=X_train.drop(['play_star_rating', 'val_star_rating'], axis=1)
X_test=X_test.drop(['play_star_rating', 'val_star_rating'], axis=1)

print ('Shape of X_train after drop ', X_train.shape)
print ('Shape of X_test after drop ', X_test.shape)

# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here

# instantiate linear regression model
regressor = LinearRegression()

# fit model on training data
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

print ("Predicated value: ", y_pred)
mse=mean_squared_error(y_test,y_pred)
print ('mean squared error: ', mse)
r2 = r2_score(y_test,y_pred)

print ('r2 score: ', r2)
# Code ends here


# --------------
# Code starts here
residual = y_test - y_pred
print (residual.shape)
print (y_test.shape)
print (y_pred.shape)

plt.hist(residual)
plt.ylabel('Frequency')
plt.xlabel('residual')
# Code ends here


