#create arrays
name_arr = []
birthdate_arr = []

#open file, iterate through and copy the first 2 words, add to fullName, copy last 3 words and add to birthdate array
with open('DOB.txt', 'r') as file:  
    for line in file:
        temp = line.strip()
        temp = temp.split(' ')

#temp vars for new strs    
        fullName = temp[0] + " " + temp[1] 
        birthdate = temp[2] + " " + temp[3] + " " + temp[4] 

#add strs to storage arrays
        name_arr.append(fullName)
        birthdate_arr.append(birthdate)


#Iterate through name list and print all names
print("Names:\n")
for fullName in name_arr: 
    print(fullName)
print("\n")

#Iterate through birthdate list and print all birthdates
print("Birthdate:\n")
for birthdate in birthdate_arr:
    print(birthdate)
print("\n")
