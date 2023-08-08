import pandas as pd

len(df)  #count number of rows
df.isnull().sum().sort_values(ascending = False) # check missing data and list down the most missing data
df.drop(colName, axis = 1) #drop columns
df.sort_values('adr',ascending=False)
df['colName'].value_counts() #return count values 

1 in range(1,16) # return True
pd.to_datetime() # convert to datetime from str template




















