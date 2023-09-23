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
model.coef_ #return coefficient

from sklearn.metrics import mean_absolute_error,mean_squared_error
MAE = mean_absolute_error(y_test, test_predictions)
MSE = mean_squared_error(y_test, test_predictions)
RMSE = np.sqrt(MSE)



#Model deployment
from joblib import dump, load
dump(model,'model.joblib')
loaded_model = load('model.joblib')

campaign = [[149,22,12]]
loaded_model.predict(campaign) #return predicted values for y

from sklearn.preprocessing import PolynomialFeatures
polynomial_converter = PolynomialFeatures(
    degree = 2
    , include_bias = 
    ,
)
polynomial_converter.transform(X) #create interaction ....
polynomial_converter.fit_transform(X)


#########Bias - variance Trade off
#Overfitting versus Underfitting
underfit = high bias, low variance, simple model 
overfit = high variance , low error on training sets but high error on test/validation sets

--> To select an ideal complexity we have to rely on the train error and test error also

###Choose degree of Polynomial ####
# Create the different order poly
# Split poly feat train/test
# Fit on train
# Store/save the RMSE for both the TRAIN and TEST
# Plot the results (error vs poly order)

train_rmse_errors = []
test_rmse_errors = []


for d in range(1,10):
    poly_converter = PolynomialFeatures(degree=d, include_bias = False)
    poly_features = poly_converter.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features,y, test_size = , random_state = )
    model=LinearRegression()
    model.fit(X_train,y_train)
    
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    train_rmse = np.sqrt(mean_squared_error(y_train,train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_test,test_pred))
    
    train_rmse_errors.append(train_rmse)
    test_rmse_errors.append(test_rmse)
    
from sklearn.linear_model import Ridge
ridge_model = Ridge(alpha = 10)
ridge_model.fit(X_train, y_train)
test_predictions = ridge_model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error
MAE=mean_absolute_error(y_test,test_predictions)
RMSE=np.sqrt(mean_squared_error(y_test,test_predictions))

from sklearn.linear_model import RidgeCV (cross validation)
ridge_cv_model = RidgeCV(alphas = (0.1,1,10), scoring = 'neg_mean_absolute_error')
ridge_cv_model.fit(X_train, y_train)
ridge_cv_model.alpha_
ridge_cv_model.coef_

from sklearn.metrics import SCORERS
SCORERS.keys() #higher is betters : transform as deafult for scores
#---> scoring = 'neg_mean_absolute_error')


from sklearn.linear_model import LassoCV
lasso_cv_model = LassoCV(eps = 0.001, n_alphas = 100, cv = 5, max_iter= 1000)
lasso_cv_model.fit(X_train, y_train)
lasso_cv_model.alpha_
test_predictions = lasso_cv_model.predict(X_test)
MAE = mean_absolute_error(y_test,test_predictions)
RMSE = np.sqrt(mean_squared_error(y_test,test_predictions))

from sklearn.linear_model import ElasticNetCV
elastic_model = ElasticNetCV(l1_ratio = [],eps = , n_alphas = , max_iter=  )
elastic_model.fit()
elastic_model.l1_ratio_






















































