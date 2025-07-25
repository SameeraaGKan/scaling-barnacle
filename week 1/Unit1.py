"""
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

input: nums (list of distinct positive integers)
output: int (a number from the list that is neither min nor max, or -1 if not found)
example:
nums = [1, 2, 3, 4, 5, 6, 7]
goldilocks_approved(nums)
output: 4

edge cases:
    nums = [1, 2, 3, 4, 5, 6, 7]
    goldilocks_approved(nums)
    output: 4


"""

def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1  # Not enough numbers to have a "just right" option

    min_num = min(nums)
    max_num = max(nums)

    for num in nums:
        if num != min_num and num != max_num:
            return num  # Return the first number that is neither min nor max

    return -1  # If no such number exists

"""



"""