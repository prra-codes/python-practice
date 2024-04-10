#20. Beginner - Lost Without a Map, Tue, 9/04/23

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    newArr = []
    for x in a:
       newArr.append(x * 2)
    return newArr