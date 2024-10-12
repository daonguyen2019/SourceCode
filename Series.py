ser.iloc[] #index
ser.loc[] #label of index
ser.head()
ser.tail()
ser.to_frame() #convert to DataFrame

ser.describe()
ser.unique()
ser.nunique()
ser.nlargest()
ser.nsmallest()
ser.value_counts()
ser.plot()
ser.astype()

ser.add_prefix() #For Series, the row labels are prefixed. For DataFrame, the column labels are prefixed.
ser.add_suffix() 
ser.diff(periods = 1) #First discrete difference of element
ser.dropna()
ser.fillna()
ser.idxmin() #Return the row label of the minimum value
ser.idxmax()    

ser.size
ser.shape
len(ser) #buil-in function
ser.count() #Return number of non-NA/null observations
ser.isna().sum() #return number of null observations
ser.sort_value() #returns a new series, sorted by values
ser.sort_index() #returns a new series, sorted by index labels

#def user_function (lambda1, lambda2)
ser.update(other_series)
ser.apply(user_function) #apply function for each value of series
ser.apply(lambda x: f"${x*24}")
ser.apply(user_function, args = (lambda2,)) #lambda1 is auto passed by the value of series
ser.map(user_dict)
ser.map(lambda a : a< 18)


#map(function, iterables) #The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.





pd.concat([ser1, ser2]) #return a new series that contain values from both series
pd.concat([ser1, ser2], ignore_index = True) #create new index, remove old index of each series
pd.concat([ser1, ser2], axis = 1) # return a dataFrame that contains 2 series
pd.concat([ser1, ser2], axis = 1, keys = ['col1', 'col2']) # return a dataFrame that contains 2 series
                    #, mapping based on index no matter the order
pd.concat([ser1, ser2], axis = 1, join = 'inner') #return just the overlap




                 








