import random
import pandas as pd
# from sklearn import prepocessing 

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)
make_list = df.Make
items = pd.Series([random.choice(make_list) for i in range(93)])
# print(make_list)

encoded_items = items. map(lambda x: make_list(x))
print(encoded_items)
# print(items)

