# Given two strings
# Return true or false if the strings are anagrams.
# Strings are Anagrams if they both contain the same exact characters

# "ab" "ba" -> True
# "aba" "ba" -> False
def is_anagram(s1: str, s2: str):
    pass

assert(is_anagram("ab", "ba")) is True
assert(is_anagram("aba", "ba")) is False
assert(is_anagram("", "")) is True
assert(is_anagram("aB", "ba")) is False
assert(is_anagram(" aa", " a a")) is False
assert(is_anagram("12", "21")) is True
assert(is_anagram("ab", " aba")) is False
