# is Anagram?

proof that using in-built functions can create lot more efficient solution.

By using `list()`: 

```python
    # create 2 lists with each parameter input
    list1, list2 = list(s1), list(s2)
```

we avoid the need to write a specific for loop for each string into array. Likewise, we can avoid writing for loops to iterate through each list to sort the elements:

```python
    # sort both lists
    list1.sort(), list2.sort()
```

This does necessarily improve the time complexity, `list()` and `sort()` still run in `O(n)`, respectively.