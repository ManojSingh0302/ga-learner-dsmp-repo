### Project Overview

 Problem statement
You are a die hard Lego enthusiast wishing to collect as many board sets as you can. But before that you wish to be able to predict the price of a new lego product before its price is revealed so that you can budget it from your revenue. Since (luckily!), you are a data scientist in the making, you wished to solve this problem yourself. This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. Your aim is to build a linear regression model to predict the price of a set.

About the Dataset:
The dataset has details of 12261 lego sets with the following 10 features
!!![container width="100%" align="center"]
![DataSetSnap](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b-183/746fdbba-1756-47e9-b627-c5f95109851b/file.png)
!!![container-end]




### Learnings from the project

 After completing this project, I was having the better understanding of how to build a linear regression model. In this project, we have applied the following concepts.

- Train-test split
- Correlation between the features
- Linear Regression
- MSE and R^2
-  Evaluation Metrics


### Approach taken to solve the problem

 **Steps**
1. Load the dataset and split it into train and test set.
2. Check the scatter_plot for different features vs target variable list_price.
3. Keeping a inter-feature correlation threshold of 0.75. If two features are correlated and with a value greater than 0.75, remove one of them.
4. Used linear regression to predict the price and checked the model accuracy using r^2 score and mse.
5. Calculate the residual and visualize the errors in the model.


