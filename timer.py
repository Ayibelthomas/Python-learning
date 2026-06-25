from time import time
def timer(func):
  def wrapper(n):
    time1 = time()
    sum = func(n)
    time2 = time()
    time_took = time2 - time1
    print(f'Time took {time_took}')
    return sum
  return wrapper

try :
    @timer
    n = int(input('\nEnter a number : '))
    def sum(n):
      sum = 0
      for i in range(1,n+1):
        sum += i
    return sum
    a = sum(n)
    print(f'The sum of {n} numbers is {a}')
except Exception as e :
  print(f'Error : {e}')
  
