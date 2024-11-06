# Anagrams are different words with same characters
def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

print(anagrams('restful', 'fluster')) # -> True