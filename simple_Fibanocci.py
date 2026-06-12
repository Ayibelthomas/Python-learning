def fibanocci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibanocci(n-1)+fibanocci(n-2)
  
n = ini(input('\nEnter the limit for number of terms:")
if n < 0 :
            print('No terms to print')
else :
              for i in range(n):
              print(fibanocci(i) ,end('\t')
              
            
        
