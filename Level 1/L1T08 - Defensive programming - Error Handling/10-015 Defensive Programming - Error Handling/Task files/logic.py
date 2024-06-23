name = str(input("What is your name? "))
age = str(input("What is your age? "))
cooldrink = str(input("What is your favorite cooldrink? "))
total_cooldrink = int(age) * 366  

if int(age) < 1:
    print("Error: Age can't be less than 1")
else:
    print("Hello " + name + ". You are " + age +
        " years old. If you drank a " + cooldrink + 
        " a day for your whole life, you would have drunk " + 
        str(total_cooldrink) + " already.") 
    
"""
Logical error in total cooldrink. Calculation is based on number of days
in a leap year. This does not account for normal tears and should 
actually by 365.
"""
