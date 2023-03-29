# Two Sum Documentation

Two Sum is a common entry level coding problem and is generally used as the main example for learning early algorithmic thinking and planning. The contrast between complexity however, once the algorithm is understood, is a reminder of how important efficient algorithms can be.

Problem:
> #### Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
> #### You may assume that each input would have exactly one solution, and you may not use the same element twice.
> #### You can return the answer in any order.

## Brute Force
Generally, this problem can be solved using a brute-force method (nested for-loops), for example:

Solution:
```python
    # consider the a given array, with unique ints
    # and a target
    arr = [3, 5, 6, 2]
    target = 7

    def two_sum( arr: List[int], target: int) -> List[int]:

        # first iteration through length of arr - 1
        # there is no need for i to iterate through entire 
        # len of arr, as j will check last element
        for i in range(len(arr)-1):

            # second iteration starting from i + 1
            # this ensures that i will never overlap with j
            for j in range(i+1, len(arr)):
                
                # comparison of values to target
                # if sum of both values equals target
                if(arr[i] + arr[j] == target):

                    # return index of both values
                    return [i, j]

        return  # safety net
```

The use of the double for loop causes the time complexity to be approx. **O(n^2)**, meaning that as `n -> infinite`, the amount of time the program will take to
reach a solution would be **(+)parabolic** and depending on the programs needs, this may be inefficient.

Double for loop in brute force solution:

```python
        # first iteration through length of arr - 1
        # there is no need for i to iterate through entire 
        # len of arr, as j will check last element
        for i in range(len(arr)-1):

            # second iteration starting from i + 1
            # this ensures that i will never overlap with j
            for j in range(i+1, len(arr)):
```

There is however a more efficient solution.

### Dictionary/Hash Map
In python a dictionary is a data structure that allows us to store paired elements, these pairs are called ***keys*** and  ***values***. By using this storage method we are able to write an algorithm that will only require one iteration of the arr, more specifically an ***enumeration()*** of arr.

This results in a faster time complexity, approx. **O(n)** time, however there is a trade-off.

Solution:

```python
    def two_sum(arr, target):

        # create an empty dictionary
        # this will be used to store the difference
        # between the target and current value
        map = {}

        # iterate through the enumerated arr
        for index, value in enumerate(arr):

            # get the difference target and value
            diff = target - value

            # if the differnce value is found in map then
            # However for the first values of index and value
            # there will be nothing in map
            # So it will just add the value and it's index to the map
            if diff in map:
                
                # return the index of current value and the index of
                # the diff value in map
                return [map[diff], index]

            # adding value and it's index to map
            map[value] = index

        return  # safety net
```

The use of ***`enumerate()`*** creates both an index and element values from `arr`
this allows us to use both these values much easier.

```python
    for index, value in enumerate(arr):
```

As the for-loop iterates, it is comparing the difference of the target value and the current value in `arr` and checks whether that difference exists within the dictionary. Note, that the first difference values will have nothing to compare to as map will be empty, therefore it will be added to the map, for other value comparisons.

Compares difference to map in Dictionary/Hash Map solution:
```python
    # if the differnce value is found in map then
    if diff in map:
    
        # return the index of current value and the index of
        # the diff value in map
        return [map[diff], index]

    # adding value and it's index to map
    map[value] = index
```

This means that only one iteration through `arr` is necessary, and thus a more efficient solution to the Two Sum problem that brute force, as `n -> infinite`.

As stated before, there is a trade-off with this solution. 

```python
    def two_sum(arr, target):
        map = {}
```

By initialising a dictionary called `map`, we are essentially reserving **memory** for this algorithm, meaning that the space complexity of this algorithm, will grow as the map size grows, as we are using memory to store, therefore the space complexity would be approx **O(n)**.

Where as the brute force solution, only has a space complexity of **O(1)**, as it only ever needs to return a list of constant size, 2, the index of both values that add to target.