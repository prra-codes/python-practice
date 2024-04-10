#18. Invert values, Tue, 9/04/23

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    newArr = []
    for x in lst:
        x = x * -1
        newArr.append(x)
    return newArr
