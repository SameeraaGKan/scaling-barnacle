# Problem 3: Secret Identity
# Write a function remove_name() to keep Batman's secret identity hidden. 
# The function accepts a list of names people and a string secret_identity 
# and should return the list with any instances of secret_identity removed.
#  The list must be modified in place; you may not create any new lists as 
# part of your solution. Relative order of the remaining elements must be maintained.

# input: a list of names and a string
# output: the list with secret_identity removed
# Plan:
# 1. Iterate through the list
# 2. If the element is equal to secret_identity, remove it
# 3. Return the list

def remove_name(people, secret_identity):
    for name in people:
        if name == secret_identity:
            people.remove(name)
            return people
# Example usage:
names = ["Abby", "Clark", "Bridget", "Wayne"]
remove_name(names, "Wayne") 
print(names)  