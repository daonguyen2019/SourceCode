import pandas as pd

pd.read_csv('../folder/file.csv') #get file from different current folder

len(df)  #count number of rows
df.isnull().sum().sort_values(ascending = False) # check missing data and list down the most missing data
df.drop(colName, axis = 1) #drop columns
df.sort_values('adr',ascending=False)
df['colName'].value_counts() #return count values 

1 in range(1,16) # return True
pd.to_datetime() # convert to datetime from str template

df.info() #show all columns and data type of these columns
df.nsmallest(n, columns) #Return the first n rows ordered by columns in ascending order
df.corr() #Compute pairwise correlation of columns, excluding NA/null values.

round(df['col'],2) = df['col'].round()































