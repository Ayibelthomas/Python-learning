name  = input("Enter your name: ")
age = int(input("Enter your age: "))
Country = input("Enter your place: ")


#if is a conditional statement that allows you to execute a block of code only if a certain condition is true.  

if age <18 :
    print("Sorry " + name + ", you are not eligible to vote.")

#elif is a conditional statement that allows you to check multiple conditions. It stands for "else if". 
# elif is used after an if statement and before an else statement. It allows you to check for additional conditions if the previous condition(s) were not true.
# You can use it to check for additional conditions if the previous condition(s) were not true.
#else is a conditional statement that allows you to execute a block of code if all the previous conditions were not true. It is used at the end of an if-elif chain to provide a default case when none of the previous conditions are met.
if Country.lower() == "india":
    print("You are from India.")
else:   
    print("You are not from India.")

if age < 18 :
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else :
    print("You are a senior citizen.")

for i in range(1,11):
    print(i,end=" ")

while age < 18:
    print("You are a minor.")
    age += 1
print("You are now an adult.")

day = input("Enter the day of the week: ")

match day.lower():
    case "monday":
        print("It's Monday, the start of the week.")
    case "tuesday":
        print("It's Tuesday, the second day of the week.")
    case "wednesday":
        print("It's Wednesday, the third day of the week.")
        if day.lower() == "wednesday":
            pass
    case "thursday  ":
        print("It's Thursday, the fourth day of the week.")
    case "friday":
        print("It's Friday, the fifth day of the week.")
    case "saturday":
        print("It's Saturday, the sixth day of the week.")
    case "sunday":
        print("It's Sunday, the seventh day of the week.")
    case _:
        print("Invalid day entered.")