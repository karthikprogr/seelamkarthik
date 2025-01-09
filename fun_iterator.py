# lambda
result = lambda x,y:x*y
print(result(10,20))

#iterator
lst1=[1,2,3,4,5,6]
itera_val=iter(lst1)
print(itera_val)
type(itera_val)

# for i in range(10):
i=[1,2,3,4,5,6,7,8]
res=iter(i) #here we are using the for loop to repeat all the times
for j in res:
  if (j>5):
    print(j+1)
# if i in res>5:
#   print(res+1)
  else:
    print("none")



#iterator
for i in range(10):
  if i>5:
    print(i+1)
  else:
    print("none")



#Generator
# without generator
def square(i):
  for i in range(i):
    i = i**2
  return i
res = square(1)
print(res)



#with generator for square of the number
def square(i):
  for i in range(i):
    i=i**2 # i+1 for the addition of the number
    yield i
square(10)
for i in square(10):
  print(i)



def sample(item):
  item = item.upper()
def low(item):
  item = item.lower()
def add(item):
  item = item+1
result=sample

print(result('hello'))