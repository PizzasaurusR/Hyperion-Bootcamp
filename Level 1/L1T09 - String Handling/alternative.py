sentence = str(input("Please type your sentence here: "))
split_sentence = sentence.split() # Create an array of the words in sentence split by " "
char_alt_str = ""
word_alt_str = [] #array to store split words
new_sentence = "" # output str for upper and lower case words str

for i in range(len(sentence)): # Search through the length of the string and check each char index 
  
    if i % 2 == 0: # if the char is in an odd position (1, 3, 5...) then capitalize

        char_alt_str += sentence[i].upper()

    else: # otherwise make the char lower case

        char_alt_str += sentence[i].lower()

for i, temp_word in enumerate(split_sentence): # search through list to check item index. I used enumerate to make the list iterable

    if i % 2 == 0: 
        word_alt_str.append(temp_word.lower()) #append new word onto str, could not make this work without append, Youtube videos were used to help this
    else:
      word_alt_str.append(temp_word.upper())

new_sentence += ' '.join(word_alt_str) # Join words with a space between them

print(char_alt_str)
print(new_sentence)

