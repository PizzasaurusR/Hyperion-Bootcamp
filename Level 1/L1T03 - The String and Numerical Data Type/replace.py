"""
set sentence variable as The!quick!brown!fox!jumps!over!the!lazy!dog.
replace "!" in sentence with " " using replace and set as new_sentence
print new_sentence
capitalize new_sentence using upper and set as capital_sentence
print capital_sentence
reverse new_sentence and set result as rev_sentence
print rev_sentence
"""

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

new_sentence = sentence.replace("!" , " ")
print(new_sentence)

capital_sentence = new_sentence.upper()
print(capital_sentence)

rev_sentence = new_sentence[::-1]
print(rev_sentence)