# Two Sum (leetcode #1)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# global arr
arr = [2, 1, 5, 3]


# brute force solution
# O(n^2) time complexity with double for loops
# O(1) space complexity
def two_sum_brute(arr, target):
    for i in range(len(arr)-1):
        
        for j in range(i+1, len(arr)):

            if(arr[i] + arr[j] == target):
                return [i, j]

print(two_sum_brute(arr, 7)) # print results


# using dictionary/hash map
# seperate arr, into index and value
# loop through each
# if the difference of target and value exists in map
# then return diff index value in map and current index
# otherwise add diff value to map
# O(n) time complexity, but O(n) space complexity
arr = [2, 1, 5, 3]
def two_sum_map(arr, target):
    map = {}

    for index, value in enumerate(arr):
        diff = target - value

        if diff in map:
            return [map[diff], index]
        
        map[value] = index

print(two_sum_map(arr, 7))  # print results