# Problem 2: Count Even Strings
# Implement a function count_evens() that accepts a
#  list of strings lst as a parameter. The function 
# should return the number of strings with an even 
# length in the list.

# UMPIRE
# input: a list of strings
# output: an integer representing the count of strings with even length

def count_evens(lst):
    num_even = 0
    for string in lst:
        str_len = len(string)
        if str_len % 2 == 0:
            num_even += 1
    return num_even

# Example::        
lst = ["hello", "world", "python", "is", "fun"]
print(count_evens(lst))  # Output: 2 (only "is" and "fun" have even length)   