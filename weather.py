import pandas as pd

#read the dataframe using panadas, as the data is seperated by spaces sep =\s+
dataframe = pd.read_csv('weather.dat', sep='\s+')
#convert the data in the columns into int
dataframe[['MxT', 'MnT']] = dataframe[['MxT', 'MnT']].apply(lambda x: x.str[:2].astype(int))
#create new column to show the differences
diff = dataframe.MxT - dataframe.MnT
#find the index of the larget difference  
x = diff.index[diff == max(diff)].tolist()
#return the day at the location of the largest difference
lisday = dataframe.loc[x][['Dy']].unstack()
#convert to string
day = lisday[0]
#Get the max spread
spread = max(diff)

print (day,spread)