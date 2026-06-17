def division(a,b):
  try:
    c = a/b
  except Exception as e :
    return f"{e} error !!"
  else :
    print("There was no error occured!!")
    return c
  finally:
    print(f"There we divied {a} with {b}")

try :
  a = int(input('Enter a number :'))
  b = int(input('Enter a second number :'))
  print(f'We get {division(a,b)}')
except Exception as e :
  print(e)
