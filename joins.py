import pandas as pd

sales_data= {
    "TransactionID" : [1,2,3,4],
    "CustomerID" : [101,102,103,104],
    "Amount" : [250,567,234,678],
    "date": ['23-2-2025','24-3-2045','12-4-2090','26-3-2020']
}
a=pd.DataFrame(sales_data)
print(a)
customer_data = {
    "CustomerID" : [101,102,346,87,9],
    "CustomerName" : ["bob","janu","ram","ravi","karthik"],
    "Age" : [29,34,23,12,45],
    "city" : ["New york","INDIA","newdelhi","hyd","china"]
}
b=pd.DataFrame(customer_data)
print(b)

#inner
print(pd.merge(a,b,on="CustomerID",how="inner"))

#outer
print(pd.merge(a,b,on="CustomerID",how="outer"))

#left
print(pd.merge(a,b,on="CustomerID",how="left"))

#right
print(pd.merge(a,b,on="CustomerID",how="right"))

# sales_df = pd.DataFrame(sales_data)
# print(sales_df)
# customer_df = pd.DataFrame(customer_data)
# print(customer_df)
# #describe
# print("Describe of sales_data: \n",sales_df.describe())
# print(customer_df.describe())
# #info
# print(sales_df.info())
# print(customer_df.info())