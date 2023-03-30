'''
My version of isAnagram on Leet code (#242)
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
s1 = "ceacarrs"
s2 = "racecars"

def is_anagram(s1: str, s2: str) -> bool:
    # check if length of strings are ==
    if(len(s1) == len(s2)):
        
        # create 2 lists with each parameter input
        list1, list2 = list(s1), list(s2)

        # sort both lists
        list1.sort(), list2.sort()

        # compare if lists have the same values in elements
        if(list1 == list2):
            return True
    return False

print(is_anagram(s1, s2))