import pandas as pd
import numpy as np

pd.options.display.max_columns = 30
pd.options.display.float_format = '{:.2f}'.format

.squeeze() #get a series out of dataFrame
pd.read_csv('../folder/file.csv', parse_date = [ListcolName]) #get file from different current folder
pd.read_csv(".tsv", sep="\t", names=[list of Column], index_col = ) #get file from tsv file
len(df)  #count number of rows
df.info() #show all columns and data type of these columns
df.describe() #df.describe(include = [])
df.dtypes

df.min()
df.max()
df.idxmin() #Return index of first occurrence of minimum over requested axis
df.idxmax() #Return index of first occurrence of maximum over requested axis
df.sum(numeric_only = True) #numeric only is using for getting just numbers
df.count() #no null value
df.size() #all value
df.mean()
df.median() 
df.mode() 
df.duplicated() #duplicated rows
df.drop_duplicated() #delete duplicated rows
df.dropna(subset = [List of Column], how = 'all', thresh = 0.5)


df.select_dtypes(include='numerics' #np.number) #Return a subset of the DataFrame’s columns based on the column dtypes. 
    #df.select_dtypes(exclude = ['object']) #select datatype for each columns, exclude object --> numerical
df.isnull().sum().sort_values(ascending = False) # check missing data and list down the most missing data
df.sort_values('colName',ascending=False)
    #df.sort_values(listColum,ascending=listOrder)
df.nlargest(n, columns) #Return the first n rows ordered by columns in descending order
df.nsmallest(n, columns) #Return the first n rows ordered by columns in ascending order
df.corr() #Compute pairwise correlation of columns, excluding NA/null values.
    #df.corr()[colName].sort_values().dropna(axis=0,subset = [colName])
df.isna().astype(int) #flag 1 for missing data
df.drop(colName, axis = 1 or axis = 'columns') #drop columns
    #df.drop(labels = 'rowIndexName', axis = 0 or axis = 'index') #drop rows, df.drop(df.index[])
df.agg(['sum', 'min']) #return sum, min for each columns
df.loc[:,df.columns!='']
    #df.loc['rowIndexName'] #return a serie, df.loc[num1:num2:step]
    #df.loc[['rowIndexName']] #return a dataFrame
df.loc[,] = value #using to update value
df.at[,] = value #using to update value, faster than loc
df[newCol] = 'value' #add static column 
df.iloc[position of index]
df.sample(frac=0.5, replace=True, random_state=1) #A random 50% sample of the DataFrame with replacement


df.insert(position, 'NewColName','value') #value is a series
df.assign(columnName = []) #add a column to a dataFrame
df.append(row) # add row to dataFrame, row needs to be in Series with Name, and index name = columns of dataFrame
    #df.append(list of row)
    #df.append(dataFrame)
df.rename(index = dict_mapper or column = dict_mapper)
df.at[rowIndex, 'col'] = new value # assign new value into a DataFrame
#==============Index & MultiIndex==============
df.index
    #df.get_loc()
    #df.index.max()
    #df.index.argmax()
    #df.index.freq = 'MS' #Month
    #df.index.duplicated()
    #If index is Datatime Index
        #df.index.quarter
        #df.index.month
        #df.index.weekofyear
        #df.index.day
        #df.index.day_name()
        #df.index.is_leap_year()
                        
df.set_index(colName, inplace = True) 
    #df.set_index(list of ColName) #MultiIndex
df.sort_index(ascending = ) #axis = 1 --> sort column
df.reindex() 

df.set_index(listCol)
df.sort_index(level = 0/1) 
df.sort_index(level = [1,0], ascending = [True, False])
df.loc[(index1, index2)]
df.loc[(index1, index2):(index1, index3)]  
df.loc[:,1990, : ] 
df.loc[:,[1990,1991], : ] = df.loc[slice(None),[1990,1991], : ]
df.iloc[] #iloc didnt care about the multiIndex
df.loc(slice(()),) #using slice object in MultiIndex, slice(None)
df.loc[pd.IndexSlice[:,[]]]
df.xs(key = '013', level = 'year' or level = 1) #Return cross-section from the Series/DataFrame.
    #select data from MultiIndex as label index
df.xs(key = (), level = (0,1))
df.index.levels
df.index.get_level_values(level=0)
df.swaplevel(2,1) #swap level of multi Index
df.reorder_levels( )
df.droplevel()
df.reset_index()

idx = df.index
idx.is_lexsorted() #Return True if the codes are lexicographically sorted.
idx.sortlevel(0, ascending=False, sort_remaining=True)
    #idx.sortlevel((0,1,2), ascending=[False,True, True])
idx.set_names() #change name of index
idx.to_flat_index() #Convert a MultiIndex to an Index of Tuples containing the level values.

df.unstack(level=) #convert a index to column --> transpose, level count from 0 to 
df.stack()

#---------------------------------

#apply function
def complicated_func():
df.apply(complicated_func, axis = 1) # 1 apply for rows - which is advantage when using apply

df[colName].replace('oldValue','newValue') 
    #df[colName].replace(['ListoldValue'],['ListnewValue']), must use list if replace None
    #df[colName].replace(regex='%',value='') #replace percentage symbol
df[colName].round() #round(df[colName],2)
df[colName].map({'R':0,'M':1})
df[colName].value_counts() #return count  values 
    #df[colName].value_counts(normalize = True) #return relative frequencies of the unique values
df[colName].unique() #return all unique values of a column
df[colName].nunique() #return Number unique values of a column
df[colName].apply(str) #--> apply string to convert numerical
df[colName].equals(df['Other colName'])  #Test whether two objects contain the same elements.
df[colName].str[0]
df[colName].astype(str) #convert to string
    #df[colName].astype('category') #convert to category if value is finite
    #df[colName].astype(np.datetime64) #convert to Date
df[colName].fillna(0)
df[colName].between() #return boolean series
df[colName].isin() #return boolean series
df[colName].isna() 
df[colName].notna() 
df[colName].quantile(#number) 
df[colName].pct_change() #return percentage change 
df[colName].mul() #multiple series
df[colName].diff(periods = 1 ) #return different compare with previous one
df[colName] = np.where(df[colName].isnull(), value1. value2)
df[colName].plot.hist(edgecolor='k').autoscale(axis='x',tight=True);

#---------------------------------------------------------------------------------

df.boxplot(showfiler = True #Remove outliers)
df.plot(subplots = True, linewidth = ,figsize = (,)) #get seperate chart in one figure
df.plot(kind = 
        , title = ""
        ,xlabel = 
        ,ylabel = 
        ,fontsize = 
        ,subplot = True #auto create subplot
        , sharex = 
        , sharey = 
        , layout = (ncol, nrow) 
        , ls='--'
        , linewidth=5
        , dashes=[3, 3]
        , ax = #where to put the chart
)
df.plot(kind = 'hist'

)
###===========================Time Series =========================================
from datetime import date, time,datetime
from dateutil import parser #pip install python-dateutil 

date_a = date(2024,9,29)
    #date_a.year, date_a.month, date_a.day
time_a = time(4,30,12,9432)
    #hour, minute, second, microsecond
time_a.isoformat() #return to normal standard
import datetime 
datetime(year, month, day, hour, min, sec)
datetime.now() #return current time
#Datetime --> strptime(string parse time), #convert to datetime object
    #datetime.strptime('2019-10-31', '%Y-%m%d')
    
pd.date_range('2000-01-01',periods = 7, freq = 'D') #create a datetime index
pd.to_datetime(df) # convert to datetime from str template
pd.to_datetime("10/11/12", yearfirst = True, dayfirst = True) # convert to datetime from str template
pd.to_datetime("10/11/12", format = '%y/%m/%d') # convert to datetime from str template
pd.to_datetime("Dec 11 2019 Meeting", format = '%b %d %Y Meeting') 
pd.to_datetime('4/7/1776',dayfirst = True)
pd.Timestamp('4th of July 1776')
    #pdts = pd.to_datetime('4/7/1776',dayfirst = True)
    #pdts.day_name()
    #pdts.days_in_month()
    #pdts.quarter 
    #pdts.isocalendar()
pd.DateOffset(days=3,hours = 4)
pd.Timedelta(days =3,hours = 4)
 
df.resample(rule = 'A').mean() #Resample time-series data. Very useful to get the picture
    #resample frequency down --> down sample, eg. D(daily) --> M (Monthly)
    #resample frequency up --> up sample, eg. D(daily) --> H(Hourly)
df.resample(rule = '8H').interpolate(method = 'linear')
df.asfreq(fill_value = )

df.shift(periods=#number, freq = 'M') #Shift index by desired number of periods with an optional time freq.
df.rolling(window=30).mean()  #moving average
df.expanding().mean()#Provide expanding window calculations, avg value till the current point
df.ewm() #provide exponential weighted
df[colName].between(date1, date2) #default include both value

df[colName].dt.strftime("%Y%m")  
df[colName].dt.day_name()  #return Monday/Tuesday...
df[colName].dt.month #return Month
df[colName].dt.year #return Year
df[colName].dt.quarter #
df[colName].dt.weekday #
 

#=======================================STRING==========================
        #regular expression: https://regex101.com/ 
df[colName].str.upper() #Series has no method upper
df[colName].str.lower()
df[colName].str.capitalize()
df[colName].str.split(to_strip = "", expand = True) # create a split for each words
df[colName].str.rsplit()
df[colName].str.lsplit()
df[colName].str.split("", expand = True) #expand = True split data
df[colName].str.replace() #replace each part of a  string in pandas ("|" meaning or)
df[colName].str.replace("second|minutes", abbrv) #def abbrv(reo): return  
df[colName].str.contains("")
df[colName].str.contains("day|week|month", na = False)
df[colName].str.contains(r "[]", regex = True)
df[colName].str.startswith('')
df[colName].str.endswith('')
df[colName].str.get() # get first elements
df[colName].str.cat('string',sep='_') #catenotation string
df[colName].str.get_dummies(sep=':') #get dummies



#=============GROUP BY=================
#Groupby --> SPLIT --> APPLY ==> COMBINE
    #Split: the data into the groups based on some criteria
    #Apply: functions to each group independently
    #Combine: the result into a new data structure

    #gbo = df.groupby(by = colName) 
        #gbo.ngroups #number of groupby
        #gbo.groups #dictionary of each group with index of row belong to each groups
        #gbo.first()#return first member of each group
        #gpo.get_group('colName of group') # return dataFrame of that group
        #itterate through group for name, group in gpo:
    #apply multiple function for a group by .agg()   

    #.groupby()
        #.agg() --> (typically) reduces the dimensions of the dataset
        #.filter() --> include/exclude without changing the dimensions
        #.transform() --> change the value in place without altering the shape
    
df.groupby(colName1)[ColName2].mean()        
df.groupby(colName1)[ColName2].agg(['min','max','mean','median']) #return multiple result for 1 column       
df.groupby(colName1).agg({'col1': ['min','max'],'col2': ['mean','median']}) #return different func for different col
df.groupby(colName1).agg(
                    min_col1 = ('col1','min')
                    ,max_col1= ('col1','max')
                    ,min_col2= ('col2','min')
                    ,max_col2= ('col2','max')                    
                    )

df.groupby(mappingfunc) #--> change dynamic function
df.groupby(colName1)[ColName2].mean()
df.groupby(colName1)[ColName2].transform(lambda value: value.fillna(value.mean())) #--> fill same value for all values missing
df.groupby(colName)['target'].mean() #return mean for each categorical variables
df.groupby(['colName1','colName2']).filter(lambda sg: sg['colName3'].sum()>...)
df.groupby().apply(lambda sg: )

#======================PIVOT=============================
    #index given  to pivot should not be duplicated
    #pivot_table = groupby + agg + multiindex
df.pivot(index = , columns = , values = )
df.melt()#npivot a DataFrame from wide to long format, optionally leaving identifiers set.
df.pivot_table(index =, columns = ,values = , aggfunc = , margins = , margins_name  = )






#===============Concat & Merge & Join ==================================
#concatening dataFrame by columns (same columns)
pd.concat([df1,df2], #ignore_index = True) #merge two dataFrame togethers
pd.concat([df1,df2,df3], #ignore_index = True) #merge three dataFrame togethers, column is not in overlap is fillied in with NA
pd.concat([df1,df2,df3], axis =1 ) 
pd.concat([df1,df2,df3], axis =1, join = 'inner'#outer is default)

df1.merge(df2, how = 'inner' #default)
df1.merge(df2, on = 'colName')
df1.merge(df2, on = 'colName', how = 'inner')
df1.merge(df2, on = 'colName', how = 'left') #left join
df1.merge(df2, on = ['colName1','colName2'])
df1.merge(df2, on = ['colName1','colName2'], how = 'i nner', suffixes = ('_suffix1','_suffix2')
pd.merge(df1,df2, left_index = True, right_index = True) #use the index as a key for joining
pd.merge(df1,df2, left_index = True, right_on = 'ColName' ) #use the index as a key from the left table 
                                                            #join with the column on the right table
df1.join(df2, on = 'colName'or'index', how = )


#Transform data
pd.transform(func)
df.apply(func)




pd.crosstab #Compute a simple cross tabulation of two (or more) factors.
pd.get_dummies(Series, drop_first = True) #return dummy variable for categorical data,add drop_first meaning drop the redundant encoding columns
pd.get_dummies(df,columns = [], drop_first = True)
pd.to_numeric(columnValue, errors = 'coerce') #convert to number

X_train['colName'], intervals = pd.qcut(X_train['colName'],q=5,labels=False,retbins=True,precision=3,duplicates='drop') #return cutting of series
X_test['colName'] = pd.cut(x = X_test['colName'], bins=intervals, labels=False)#cut series by inverval
df.groupby(['year','month','market'])['disbursed_amount'].sum().unstack().plot() #unstack to pivot data with column is market
    








































  






































