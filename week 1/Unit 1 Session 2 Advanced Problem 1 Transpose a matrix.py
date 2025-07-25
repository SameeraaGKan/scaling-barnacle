"""
Problem 3: Remove Duplicates
Write a function remove_dupes() that accepts a sorted array items, 
and removes the duplicates in-place such that each element appears only once.
 Return the length of the modified array. You may not create another array; 
 your implementation must modify the original input array items.

 
 Plan:

 1. intialize a variable mod_len to 1
 2. loop through the array starting from index 1
 3. check if the current element is the same as the previous element
 4. if it is not the same, increment mod_len and set the element at mod_len - 1 to the current element
"""
# add comments for each line of code
def remove_dupes(items):
    mod_len = 1  # Initialize the modified length to 1
    for i in range(1, len(items)):  # Loop through the array starting from index 1
        if items[i] != items[i - 1]:  # Check if the current element is different from the previous one
            items[mod_len] = items[i]  # Update the element at mod_len with the current element
            mod_len += 1  # Increment the modified length
    return mod_len  # Return the modified length

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
print(remove_dupes(items))

items = ["extract of malt", "haycorns", "honey", "thistle"]
print(remove_dupes(items))