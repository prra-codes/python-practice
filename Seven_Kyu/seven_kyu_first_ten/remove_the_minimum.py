#24. Remove the minimum, Wed, 10/04/23

# The museum of incredibly dull things

# The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

# Task

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples

# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

def remove_smallest(numbers):

    if numbers == []:
        return []
    copied_numbers = numbers.copy()

    smallest_num = min(copied_numbers)

    # The method index() returns the lowest index in the list where the element searched for appears

    smallest_index_num_appears = copied_numbers.index(smallest_num) 

    # The pop() method removes the element at the specified position.
    copied_numbers.pop(smallest_index_num_appears)

    return copied_numbers

print(remove_smallest([2, 2, 1, 2, 1]))