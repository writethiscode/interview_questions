# Given two strings
# Return true or false if the strings are anagrams.
# Strings are Anagrams if they both contain the same exact characters

# "ab" "ba" -> True
# "aba" "ba" -> False
def is_anagram(s1: str, s2: str):
    # Time Complexity = o(n)

    if len(s1) != len(s2):
        return False

    char_count = {}

    for char in s1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    for char in s2:
        if char not in char_count:
            return False
        
        if char_count[char] == 1:
            del char_count[char]

    return char_count == {}

assert(is_anagram("ab", "ba")) is True
assert(is_anagram("aba", "ba")) is False
assert(is_anagram("", "")) is True
assert(is_anagram("aB", "ba")) is False
assert(is_anagram(" aa", " a a")) is False
assert(is_anagram("12", "21")) is True
assert(is_anagram("ab", " aba")) is False
