class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        l = 0
        r = n-1

        while l < r: # Two pointers approach
            summ = numbers[l] + numbers[r] # Calculate the sum of the two pointers
            if summ == target: # If the sum matches the target
                return [l + 1, r + 1] # Return 1-based indices
            elif summ < target: # If the sum is less than the target, move the left pointer up
                l += 1 # Move left pointer to the right
            else: # If the sum is greater than the target, move the right pointer down
                r -+ 1 # Move right pointer to the left
