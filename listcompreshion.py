list=[1,2,3,4]
# res=[i for i in list]
# print(res)

# list1=[i+1 for i in range(1,20)]
# print(list1)

# res=[ i for i in list if i%2==0]
# res1=[ j for j in list if j%2!=0]
# print("even number",res)
# print("odd number",res1)

# words = ["Lower","a","python"]
# lower = [i for i in words]
# print(lower)


# words = ["Lower","a","python"]
# lower = [i.lower() for i in words]
# lower = [i.upper() for i in words]
# print(lower)

# keys = ["names","age","city"]
# values=["banglore",25,"hyderbad"]
# list=[i for i in list]
# dict1 = {k:v for k,v in zip(keys,values)}
# print(dict1)

#tuples
import math
num = [1,4,9]
sq=tuple(math.sqrt(i) for i in num)
print(sq)

