"""
get input str from user and assign as str_manip
print length of str_manip assign as str_len
isolate last char in str_manip and assign to new var last_char
replace all of the same char in str_manip with '@'
new str will be rep_str
print rep_str
assign new var str_rev to be the last 3 digits of str_manip in reverse
print str_rev
assign new var first_three to be the first 3 char from str_manip
assign new var last_two to be the last 2 chars in str_manip
concat first_three and last_two and assign new var str_combo
print str_combo
"""

str_manip = input("Please type any sentence in here: ")
str_len = len(str_manip)
print(str_len)

last_char = str_manip[str_len - 1]
rep_str = str_manip.replace(last_char, "@")
print(rep_str)

str_rev = str_manip[str_len - 1: str_len - 4: -1]
print(str_rev)

first_three = str_manip[0:3]
last_two = str_manip[str_len - 2:]

str_combo = first_three + last_two
print(str_combo)

