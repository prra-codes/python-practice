#29. Find the middle element, Wed, 10/04/23

# As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

# The input to the function will be an array of three distinct numbers (Haskell: a tuple).

# For example:

# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.

# Another example (just to make sure it is clear):

# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

def gimme(input_array):
    list_copy = input_array.copy()
    smallestNum = min(list_copy)
    largestNum = max(list_copy)

    for elem in input_array:
        if elem == smallestNum:
          list_copy.remove(smallestNum)
        if elem == largestNum:
          list_copy.remove(largestNum)

    middle_element = list_copy[0]
    
    return input_array.index(middle_element)


print(gimme([5, 10, 14]))