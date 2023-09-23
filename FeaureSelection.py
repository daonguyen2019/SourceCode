#Feature selection method
#1. Filter method
    #Variance
    #Correlation
    #Univariate selection
    
  #Filter methods has two step procedure:
    #rank features according to a certain criteria
    #select the highest ranking features
   
  #Feature scores on various statistical tests:
      #Chi square/ Fisher score
      #Univariate parametric tests (anova)
      #Mutual information
      #Variance
        #constant features
        #Quasi-constant features

#1. Filter method - basic methods
    #constant features
            #same values for all observations
            #no discrimination power
            #How to remove constant variables
                #varianceTreshold-skearn:
                    #store constant features
                    #Numerical variables
                #std()- Pandas:
                    #Quick
                    #Doesnt store the constant variables
                    #Numerical only
                #nunique()-Pandas:
                    #Quick
                    #Doesnt store the constant variables
                    #Numerical/categorical         
    #Quasi-constant features
            #same values for almost all observations
            #How to remove Quasi-constant variables
                #varianceTreshold-skearn:
                #value_counts()-Pandas:        
                
    #Duplicated features
        #-->Duplicate features  after one hot encoding
        
#2. Correlation

    #--> refer to the degree to which a pair of variables are linearly related
        #Pearson's correlation (linear relationship)
        #Spearman's rank correlation
        #Kendall rank correlation
    
    # method to determine correlation coefs
        pd.DataFrame.corr(method = 'pearson'/'kendall'/'spearman', min_periods = 1)
    #Method 1 : to remove features, scan features as they appear
        #if a feature is correlated with the feature we are evaluating, we remove it
            #Fast but might remove an important feature
    #Method 2: 
        #_identify groups of correlated features
        #_select the most predictive feature
                #build small ML using featires in the groups
                #other criteria such as Number of missing values
        #_discard the rest


        
    





           
        
  













        
#2. Wrapper methods
    #Forward selection: add 1 feature at a time
    #Backward selection: removes 1 feature at a time
    #Exhaustive selection: searches acorss all possible feature combinations
  #use predictive machine learning models to score the feature subset
#3. Embedded methods
   #LASSO
   #Tree importance

#Some packages for feature selection
    -scikit learn
    -MLxtend
    -Feature engine
    
    .fit() --> finds important features
    .transform() --> transform data
                    . removes unwanted features



from sklearn.feature_selection import VarianceThreshold







        








                    

 