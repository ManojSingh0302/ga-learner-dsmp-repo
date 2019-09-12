# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#print (data.head())
data['Gender'].replace('-', 'Agender',inplace=True)
gender_count = data['Gender'].value_counts()

#print ('gender_count', gender_count)
gender_count.plot.bar() 
plt.title('Bar Graph for Gender')
plt.ylabel('Count of Gender')
#Code starts here 




# --------------
#Code starts here
alignment= data['Alignment'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(alignment, explode = (0.05,0.05,0.05))
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
print (sc_df.shape)
#sc_df = data[:,['Strength','Combat','Intelligence']]

sc_covariance = np.cov(sc_df.Strength, sc_df.Combat)
sc_covariance= sc_covariance[0][1]
print (sc_covariance)
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson= sc_covariance/ (sc_strength * sc_combat)
print('sc_pearson', sc_pearson)


ic_df = data[['Intelligence','Combat']]
print (ic_df.shape)
ic_covariance = np.cov(ic_df.Intelligence, ic_df.Combat)
ic_covariance= ic_covariance[0][1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson= ic_covariance/ (ic_intelligence * ic_combat)
print ('ic_pearson',ic_pearson)


# --------------
#Code starts here
total_high = data.Total.quantile(0.99)
print (total_high)

super_best = data [ data.Total> total_high]
print (super_best.head())

super_best_names = super_best.Name.tolist()
print (type(super_best_names))
print (super_best_names)


# --------------
#Code starts here
#fig, ax_1, ax_2, ax_3 = plt.subplots(nrows = 1 , ncols = 3, figsize=(15,15))

ax_1 = data.Intelligence
ax_2= data.Speed
ax_3= data.Power


plt.boxplot ([ax_1, ax_2, ax_3])


