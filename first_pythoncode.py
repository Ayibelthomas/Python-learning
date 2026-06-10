# Variable is a container that holds data values. In Python, 
# variables are created when you assign a value to them. 
# The equal sign (=) is used to assign values to variables.
#  The variable name should be descriptive and should follow the naming conventions.``
name = 'Ayibel Thomas' # This is a string 
age = 23 # This is an integer
salary = 16445.45 # This is a float
is_working = True # this is a boolen
experience = ['Python','java','c++'] # this is a list
companys = ('Google','Meta','Amazon') # this is a tuple
skills = {'Python','java','c++'} # this is a set
domains = {"Database" : "SQL","Web Development":"Django","Data Science":"Pandas"} # this is a dictionary
if (is_working ==True ):
    print(f"The name of the employee is {name} \n Age is {age}\n and the salary is {salary}")
else:
    print(f"{name} is not working")
print(experience)
print(companys)
print(skills)
print(domains)
print(type(name),type(age),type(salary),type(is_working),type(experience),type(companys),type(skills),type(domains))
