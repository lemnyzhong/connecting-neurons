first_set = set([1, 2, 4, 5, 10, 19])
second_set = set([1, 2, 3, 6, 7, 8, 19])

# intersection = first_set & second_set
def using_intersection(set1, set2):
    print(set1.intersection(set2))

using_intersection(first_set, second_set)