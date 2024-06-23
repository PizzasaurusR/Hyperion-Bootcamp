# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])
        
        '''
        changed k to key to print the right value.
        If possible in my review could you answer this question:
        Would it have been better to change this to return and then printed the outcome later?
        Like this:
        def print_values_of(dictionary, keys):
            for key in keys:
            return(dictionary[key])

        keys = "lisa, bart, homer".split(", ")

        phrases = print_values_of(simpson_catch_phrases, keys)

        for phrase in phrases:
            print(value)
        '''

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", #Changed ' to " " - Ramiz 
                         "maggie": "(Pacifier Suck)"
                         }

'''
Ramiz:
create keys list to feed into function
took string and split using ", " to create list

'''
keys = "lisa, bart, homer".split(", ")

print_values_of(simpson_catch_phrases, keys) #used keys instead of using the str when calling function - Ramiz

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

