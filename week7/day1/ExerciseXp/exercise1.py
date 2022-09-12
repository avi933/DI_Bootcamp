import importlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  dateutil.parser import parser

# # 1
# def numpy_array(start,length,step):
#     length = ((length)*step)+start
#     return np.arange(start,length,step)
# # print(numpy_array(0,10,3))

# #2 Drop all nan values from the following numpy array.
# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# # print(a)
# new_a = a[~np.isnan(a)]
# # print(new_a)

# # 3 Create a random numpy array that has a shape of (5, 6) 
# # filled with integers between 1 and 100.
# array = np.random.randint(100,size=30)
# array = array.reshape(5,6)
# print(array)
# #Then compute the maximum int for each row in the array
# print(np.amin(array, axis=0) )
# print(np.amin(array, axis=1) )
# print(np.amin(array, axis=2) )
# print(np.amin(array, axis=3) )
# print(np.amin(array, axis=4) )

# #4 use a pandas Series function to find the unique values 
# # and their frequencies of the following Series:
# #series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# print(series.value_counts())

#5 Get the day of month, week number, day of year and day of week from this pandas series
# series = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
# series = series.map(lambda x: parser(x))
# print(series)
# print("day of month")
# print(series.dt.day.tolist())
# print("day of year:")
# print(series.dt.dayofyear.tolist())
# print("week Number:")
# print(series.dt.isocalendar().week.tolist())
# print("day of week")
# print(series.dt.day_of_week.tolist())

#6
df = pd.read_csv ('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv') 
df.rename (columns= {'Type':'TypeOfCar'},inplace = True)
# print(df.info())
# print(df.head(10))

print(df.isnull().sum().idxmax())



