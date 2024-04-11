#23. Two to One, Wed, 10/04/23

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:

# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    new_str = a1 + a2
    combinedlist = list(new_str)
    distinctlist = []

    for x in combinedlist:
        if x in distinctlist:
          pass  # Don't do anything
        else:
            distinctlist.append(x)
    distinctlist.sort()
    distinct_string = "".join(distinctlist)
       
    return distinct_string
    
print(longest("king", "dragon"))