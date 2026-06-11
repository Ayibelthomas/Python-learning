Template = ''' 
Dear {} ,
      Thankyou for applying in {} for the role {} .After careful consideration we are {} to inform you that we have 
      decided to {} with your application.{}
      Thankyou
      {}
'''
name =   input("Name = ")
cname =  input("Company Name = ")
role = input("Role = ")
action = input("Select one (Slected/Rejected) = ")
if action.lower() == "selected" :
  r = "happy"
  f = "move forword"
  t = "You will get another mail for further steps "
  print(Template.formate(name,cname.capitalize(),role,r,f,t,cname))
elif action.lower() == "rejected" :
  r ="sorry"
  f ="not move forword"
  t = "You will be in our priority list"
  print(Template.formate(name,cname.capitalize(),role,r,f,t,cname))
else :
  print("Error...!!")
  
