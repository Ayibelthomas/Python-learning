def square(num):
  return x**2
num_list = [] 
try :
  limit = int(input("Enter a limit for the list :"))
  while limit > 0 :
    value = int(input("\n Enter a value :"))
    num_list.append(value)
    limit -= 1
  print(list(map(square,num)))
except Exception as e :
  print(f"Error : {e}")
  
