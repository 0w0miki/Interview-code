# Length of Last Word
s = "a "
words = s.split()
# get the last word
word = words[-1:]
if len(word) > 0:
    # remove all non-desired characters
    result = word[0].strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return len(result)
else:
    return 0
