#27. Anagram Detection, Wed, 10/04/23

def is_anagram(test, original):

    if len(original) != len(test):
      return False
    lowercase_test = test.lower()
    lowercase_original = original.lower()

    lowercase_test_arr = list(lowercase_test)
    lowercase_original_arr = list(lowercase_original)

    lowercase_test_arr.sort()
    lowercase_original_arr.sort()

    for index, char in enumerate(lowercase_original_arr):
        if char != lowercase_test_arr[index]:
           return False
          
    return True
    

print(is_anagram("Superman", "Mansuper"))


# A solution I saw on Codewars: 

# def is_anagram(test, original):
#     return sorted(original.lower()) == sorted(test.lower()), their solution is so quick... 