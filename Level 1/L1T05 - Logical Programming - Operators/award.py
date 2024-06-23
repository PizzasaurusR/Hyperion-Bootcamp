swim_time = int(input("What was your swimming time in minutes: "))
cycl_time = int(input("What was your cycling time in minutes: "))
run_time = int(input("What was your running time in minutes: "))
qual_time = 100
total_time = swim_time + cycl_time + run_time

if total_time <= qual_time:
    print("Amazing! You have been awarded Provicial Colours!")

elif (total_time > qual_time) and (total_time <= (qual_time + 5)):
    print("Well done! You have been awarded Provicial Half Colours!")

elif (total_time > (qual_time + 5)) and (total_time <= (qual_time + 10)):
    print("Good job! You have been awarded a Provicial Scroll!")

else: 
    print("Sorry, you did not qualify.")