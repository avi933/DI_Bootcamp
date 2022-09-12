import pandas as pd
import numpy as np

df_original = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# print(df)
# print(df.shape) # give the data size
# print(df.info()) # return the data type
# print(df.species.unique()) #select distinc
# print(df[df.species == 'setosa']) # where condition
# print(df.sort_values('sepal_length', ascending=False)) #sort by descending order
# print(df.groupby('species').apply(np.mean)) #groupping

#Using the Iris DataFrame, print out the 50th row.
print(df.iloc[49:50])

# Get the 50th to 60th row of the Iris DataFrame skipping every other row 
# return a new DataFrame of just the species, petal_length, and petal_width
df = (df_original.iloc[50:60])
new = df[df.index % 2 == 0]
print(new[['species', 'petal_length','petal_width']])

#  Group the data by species and get the median and the sum of sepal_length for each group
df = df_original
print(df.groupby('species').agg(['median','sum']))