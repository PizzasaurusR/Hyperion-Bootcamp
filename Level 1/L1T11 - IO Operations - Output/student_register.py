number_of_students = int(input('How many students are registering?: '))

with open('reg_form.txt', 'a') as file:
    
    for i in range(number_of_students):
        temp = input('Please enter the students ID: ')
        file.write(temp)
        file.write('\n\n--------------------\n') #extra line space added for clarity when in actual use