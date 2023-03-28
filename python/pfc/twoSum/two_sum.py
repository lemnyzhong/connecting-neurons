# Two Sum (leetcode #1)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# brute force solution
# O(n^2) complexity with double for loops
def two_sum_brute(arr, target):
    d = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] + arr[j] == target):
                d.append(i)
                d.append(j)
    return list(set(d))

print(two_sum_brute([2,7,3,6,5, 8, 1], 9))