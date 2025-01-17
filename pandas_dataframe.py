from google.colab import files
import pandas as pd
upload=files.upload()
aaa=list(upload.keys())[0]
df=pd.read_csv(aaa)
df.head(20)
df.head() #code to show the first 5 rows
df.head(20) # code to show the first 20 rows
df.tail(120) #code to show the last 20 wors
df.iloc[[1,3,5,7]]
df.loc[[1,3,5,7]]
df.iloc[1:20,2:5] #filter a datafrmae and print 15 rows wors starts from 5 and column nam should be city and country
df.head(10)
df.iloc[1:50,2:5] #iloc is used to specify the specific index 1:50(rows), 2:5(columns)
#filter the dataframe with rows and columns by using iloc rows starting from 5 to 60
df.iloc[5:60,4:7]
df.describe()
df.shape[0]
# company name as "Vega-Gentry"
# data=df['First Name'] == 'Preston'
# print(data)
# df['First Name'] == 'Preston'
df['Company'] == 'Vega-Gentry' #
df.drop('Phone 2',axis =1) #deleting the phone number
df.isnull()










# importing the module
import pandas as pd

# creating a sample dataframe
data = pd.DataFrame({
    'Brand': ['Maruti', 'Hyundai', 'Tata',
              'Mahindra', 'Maruti', 'Hyundai',
              'Renault', 'Tata', 'Maruti'],
    'Year': [2012, 2014, 2011, 2015, 2012,
             2016, 2014, 2018, 2019],
    'Kms Driven': [50000, 30000, 60000,
                   25000, 10000, 46000,
                   31000, 15000, 12000],
    'City': ['Gurgaon', 'Delhi', 'Mumbai',
             'Delhi', 'Mumbai', 'Delhi',
             'Mumbai', 'Chennai', 'Ghaziabad'],
    'Mileage': [28, 27, 25, 26, 28,
                29, 24, 21, 24]
})

# displaying the DataFrame
display(data)
dict1={'Customer_id':[1,2,3,4,5,6],'Product':['Oven','Oven','Oven','Television','Television','Television']}
df1=pd.DataFrame(dict1)
df1
dict2={'Customer_id':[2,4,6,7,8],'State':['telangana','ap','ts','ts','ap']}
df2=pd.DataFrame(dict2)
df2
#inner join
pd.merge(df1,df2,how='inner',on='Customer_id')
#outer join
pd.merge(df1,df2,how='outer',on='Customer_id')
#left
pd.merge(df1,df2,how='left',on='Customer_id')
#right
pd.merge(df1,df2,how='right',on='Customer_id')