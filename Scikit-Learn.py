#Scikit-learn

#statsmodels

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = , random_state = )

from sklearn.model_family import ModelAlgo
mymodel = ModelAlgo(param1,param2)
mymodel.fit(X_train,y_train)
predictions = mymodel.predict(X_test)

from sklearn.metrics import error_metric
performance = error_metric(y_test,predictions)
 
#Evaluation metric for Regression
    #Mean Absolute Error (MAE)
        #average of absolute diff between predicted values & actual values  
    #Mean Squared Error (MSE)
        #larger errors are punished. Problem with units because of squared
    #Root Mean Square Error (RMSE)
        #most popular
    
#Residual plots
      #should be random and close to a normal distribution
      #show distribution of residual
      #show relation between residual and actual y values
       
       sns.scatterplot(x=y_test, y =residuals )
       plt.axhline(y=0,color = 'r',ls='--')
       sns.displot(residuals)

#normal practice
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
model.predict(X_test)












