'''
Program that gets an input for a list of integers and returns the 
largest number in the list.

My idea here is to start with the last element in the list as my 
base case. Then I want to compare the number in position[i] to 
the number in position[i + 1].

If the number in position[i] is greater than the number in 
position[i + 1], then you swap the numbers and repeat the process. 
When i = len(numbers_list - 1), you have reached the end of the list and 
the number in position[0] is the largest.

If the number in position[i] is smaller than the number in position
[i + 1], then you simply move to position[i + 1] and start comparing
again.

This is the only way I could figure out how to do this.

I'll be honest I don't know why the largest number keeps moving to the
front but it always happens and I have adjusted my code to print this 
result.

Please note: I used some of the functions from the previous task
in this one. I don't think this is plagiarizing because it's all 
my own work. Plus you know, work smart not hard. I mean I just
finished working out how to get a guaranteed list of numbers.

Added to this I did use a while loop when converting my list 
to int. The problem itself was still solved using recursion but
in an attempt to create a more robust program I ended up 
keeping the while loop in.
'''
#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------

def get_numbers_list():
    '''
    This function gets user input for the number list.
    Input is taken in as string and then converted into a list/array.

    This is an updated more efficient way of getting a list of ints I 
    think. My logic is that this is the only section with an input and 
    the only place I will have to manipulate the str.
    '''
    while True:
        list_of_numbers = input("Please enter a list of numbers separated by "
                                "spaces:\n"
                                "Eg 1 2 3 6 7 5 10 8 4 9 11...\n")
        
        str_numbers_list = list_of_numbers.strip().split()
        
        try:
            int_numbers_list = [int(num) for num in str_numbers_list]
            return int_numbers_list
        except ValueError:
            print("Invalid input detected in numbers list. Remember to input "
                  "digits only e.g., 1 2 3")
            continue

def compare_and_swap(numbers_list, index):
    '''
    This is a recursive bubble sort function.

    This function will compare numbers_list[index] to 
    numbers_list[index + 1].

    If numbers_list[index + 1] > numbers_list[index], then:
    Swap the numbers.

    Changed this function to recursively call itself. If it doesn't 
    call itself again then the sort only does on pass of the list and 
    doesn't actually sort the entire list.

    The last element in the list is meant to be the biggest but its 
    always teh first. Code adjusted to display this instead of the last
    element.
    '''
    # Checks that we aren't trying to access invalid indexes
    # Also stops recursion.
    if index < 0:  
        return
    
    if (
        index < len(numbers_list) - 1 and # Check for valid index
        numbers_list[index] < numbers_list[index + 1]
        ):
        numbers_list[index], numbers_list[index + 1] = (
            numbers_list[index + 1], numbers_list[index])

    # Call the function after the swap to check list elements again.    
    compare_and_swap(numbers_list, index - 1)

def recursive_sort(numbers_list, end_point):
        '''
        This function takes a bubble sort function and does a full pass
        on the numbers_list. This function will run repeatedly until it
        reaches the specified end_point. 

        The function recursively calls the sort function to achieve this
        '''
        # Check to see if we have reached the last element
        if end_point == 0:
            return
        # Start compare_and_swap at the first element in the list
        compare_and_swap(numbers_list, end_point - 1)  
        recursive_sort(numbers_list, end_point - 1)  
        # Recursively call with the next index position

def get_largest_number(numbers_list):
    '''
    This function calls the recursive_sort function to sort the list of 
    elements and then returns the first. This will be the largest
    element after the sort.   
    '''
    #Feed numbers_list into sort function
    recursive_sort(numbers_list, len(numbers_list) - 1)
    return numbers_list[0]

#----------------------------------------------------------------------
# MAIN PROGRAM
#----------------------------------------------------------------------

numbers_list = get_numbers_list()
largest_number = get_largest_number(numbers_list)
print(numbers_list)
print(f"The largest number in the list is: {largest_number}")
