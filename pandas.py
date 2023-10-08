import pandas as pd

pd.read_csv('../folder/file.csv') #get file from different current folder

len(df)  #count number of rows
df.isnull().sum().sort_values(ascending = False) # check missing data and list down the most missing data
df = df.drop(colName, axis = 1) #drop columns
df.sort_values('adr',ascending=False)
df['colName'].value_counts() #return count  values 

df['Target'] = df['Label'].map({'R':0,'M':1})


1 in range(1,16) # return True
pd.to_datetime() # convert to datetime from str template
df.info() #show all columns and data type of these columns
df.nsmallest(n, columns) #Return the first n rows ordered by columns in ascending order
df.corr() #Compute pairwise correlation of columns, excluding NA/null values.
df.corr()[colName].sort_values()

round(df['col'],2) = df['col'].round()

df = df.dropna(axis=0,subset = [colName])
df[listCol] = df[listCol].fillna(0)
df[listCol] = df[listCol].fillna('None')

df.groupby(colName1)[ColName2].mean()
df[colName] = df.groupby(colName1)[ColName2].transform(lambda value: value.fillna(value.mean())) --> fill same value for all values missing
df[col] = df[col].apply(str) --> apply string to convert numerical

pd.get_dummies(Series, drop_first = True) --> return dummy variable for categorical data, add drop_first meaning drop the redundant                                                       encoding columns
pd.select_dtypes(include = ['object']) --> select datatype for each columns
pd.select_dtypes(exclude = ['object']) --> select datatype for each columns, exclude object --> numerical

pd.concat([list df], axis = 1) --> 

df.at[rowIndex, 'col'] = new value --> assign new value into a DataFrame




































  






































