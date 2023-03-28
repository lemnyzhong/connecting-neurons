first_set = set([1, 2, 4, 5, 10, 19])
second_set = set([1, 2, 3, 6, 7, 8, 19])

# copy method
third_set = first_set.copy()
print(third_set)


# returns the common element values in 2 sets
# uses & or .intersecton()
def get_intersection(set1, set2):
    return set1 & set2
    # return set1.intersection(set2)

print(get_intersection(first_set, second_set))


# returns the non common element values in 2 sets
# uses '-' or .difference()
def get_difference(set1, set2):
    return set1 - set2
    # return set1.difference(set2)

print(get_difference(first_set, second_set))
print(get_difference(second_set, first_set))


fourth_set = set([4, 5, 6])
fifth_set = set([1, 2, 3, 4, 5, 6])

# returns bool if set is a subset of second set
# uses .issubset()
def get_issubset(set1, set2):
    return set1.issubset(set2)

print(get_issubset(fourth_set, fifth_set))
print(get_issubset(fifth_set, fourth_set))