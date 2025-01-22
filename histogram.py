# -*- coding: utf-8 -*-
"""histogram.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uyZTFSqfHJVVTjfUA-WGPnrEOmkcOLTU
"""

import matplotlib.pyplot as plt
#sample data: a small set of values
data = [5,7,7,8,9,10,10,11,12,11,11]
#create the histogram
plt.hist(data,bins=10,edgecolor="black")
#set the title and lables for the plot

plt.title("Simple histogram example")
plt.xlabel("Numbers")
plt.ylabel("Count")

plt.show()

import matplotlib.pyplot as pt
import pandas as pd
import seaborn as sns
datf = pd.DataFrame({"Season 1":[7,7,4,3,2],
                     "Season 2":[2,3,5,6,7]})
p = sns.histplot(data = datf)
p.set(xlabel = "X Label value",ylabel="y label value")
pt.show()

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
data = np.random.randint(20,81,1000)
plt.hist(data, bins=15, edgecolor="black", color='Skyblue')

plt.title("histogram of cancer patients age distribution")
plt.xlabel("Age")
plt.ylabel("no. of patients")
plt.show()


#task 4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "semester" : ['sem 1','sem 2'],
    "hours_studied": [6,8]
}
df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
sns.boxplot(x='semester',y='hours_studied',data=df)
plt.title("Student performance: hours studies by semester")
plt.xlabel("semester")
plt.ylabel("hours studied")
plt.show()


