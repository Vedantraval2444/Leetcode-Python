# Creating a two sum function to find indices of two numbers that add up to a target value
# Example usuage:
nums = [2, 11, 15, 7]
target = 9

# Acually running the function
def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums): # Check one by one number in the list
        if target - num in hash_map: # Check if the complement exists in the hash_map
            return [hash_map[target - num], i] # If it exists, return the indices
        hash_map[num] = i # If no such pair exists, return an empty list
        
    return []

print(two_sum(nums, target))