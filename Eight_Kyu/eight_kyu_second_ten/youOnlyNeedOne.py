#17. You only need one - Beginner, Tue, 9/04/23

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    for x in seq:
        if x == elem:
            return True
    return False