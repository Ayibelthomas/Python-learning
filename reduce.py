from functools import
def division(a,b):
  return a/b
list = [1,2,3,4,5,6,7,8,9,10]
sum = reduce(lambda x,y:x+y,list)

print(f'Sum of numbers in the list is :{sum}')
divi = reduce(division,list)
print(f"\nWhen divide all consicutive numbers we will get : {divi}")
