user_name = input("Please enter your full name: ")
user_name_len = len(user_name)

if user_name_len == 0:
    print("You haven't entered anything. Please enter your full name")
elif user_name_len < 4:
	print("You have entered less than 4 character. Please make sure that you have entered your name and surname")
elif user_name_len > 25:
      print("You have entered more than 25 character. Please make sure that you have only entered your full name.")
else:
      print("Thank your for entering your name.")

