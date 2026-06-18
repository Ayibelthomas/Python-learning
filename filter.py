def ageVlidation(items):
  name , age = items
  return age > 18
people = {}
try :
  limit = int(input('\nEnter a limit : '))
  while limit > 0 :
    name = input("\n Enter name :")
    age  = int(input("\nEnter age :")
    if age > 100 or age < 0:
               continue
    people[name] = age
    limit -= 1
  print(f'\nPeople in the list {people}')
  print(f'\nEligible people for voting are : {dict(filter(ageVlidation,people.items()))}')
