#32. Find the stray number, Wed, 10/04/23

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.

# Complete the method which accepts such an array, and returns that single different number.

# The input array will always be valid! (odd-length >= 3)

# Examples

# [1, 1, 2] ==> 2
# [17, 17, 3, 17, 17, 17, 17] ==> 3

def stray(arr):
    first_num = arr[0]

    arrOne = []
    arrTwo = []

    for x in arr: 
        if x == first_num:
            arrOne.append(x)
        else:
            arrTwo.append(x)
        
    if len(arrOne) == 1:
        return arrOne[0]
    else:
        return arrTwo[0]
    


# Found this in solutions after I solved it:

# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x

# Turns out in Python there is a count function


    