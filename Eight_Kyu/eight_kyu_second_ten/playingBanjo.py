# 11. Are You Playing Banjo?,  Tue, 9/04/23

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.

def are_you_playing_banjo(name):
    lowercaseName = name.lower()
    if lowercaseName[0] == "r" or lowercaseName[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
print(are_you_playing_banjo("Anime"))