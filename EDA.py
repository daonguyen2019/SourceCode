df = df.fillna(0) #fill 0 for NA
df.describe()
df.shape # size of dataFrame
df.to_csv('fileName.csv', index = False)

