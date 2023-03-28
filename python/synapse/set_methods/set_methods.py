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

# returns bool if set is superset of second set
# uses .issuperset()
def get_issuperset(set1, set2):
    return set1.issuperset(set2)

print(get_issuperset(fifth_set, fourth_set))

sixth_set = set([1, 2, 3])
seventh_set = set([4, 5, 6])

# returns bool if no items in two sets are common
# uses .isdisjoint()
def get_isdisjoint(set1, set2):
    return set1.isdisjoint(set2)

print(get_isdisjoint(sixth_set, seventh_set))


eighth_set = set([1, 10, 25, 3, 4])
ninth_set = set([4, 5, 6, 7])

# joins 2 sets in order, common values are not repeated
def get_union(set1, set2):
    return set1.union(set2)

print(get_union(eighth_set, ninth_set))

# random pop, removes a random element from set
print(ninth_set.pop())
print(eighth_set.pop())
print(ninth_set.pop())
