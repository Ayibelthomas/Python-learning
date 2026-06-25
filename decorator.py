def logger(func):
  def wrapper(age):
    print('\nWe are going to check to check eligibility for voting!')
    func(age)
  return wrapper
age = int(input("\n Enter your age :")

def ageVlidation(age):
  if age > 18:
    print(f'You are {age} years old and you are eligible..!')
  elif age == 18 :
    print(f'You are {age} years old so you have to wait one more year')
  else :
    print(f'You are {age} years old so you are not eligible!!!')

ageVlidation(age)
