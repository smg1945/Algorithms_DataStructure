# This pattern uses objects or sets to collect values/frequencies of values

# This can often avoid the need for nested loops of O(N^2) operations with arrays/string

# Q1) Write a function called same, which accepts two arrays. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.

# my solution: (Time complexity: O(n^2))

def same(a=list, b=list):
    if len(a) != len(b):
        return False
    for i in a:
        if i ** 2 in b:
            b.remove(i ** 2)
            pass
        else:
            return False
    return True


# Frequency Counter Pattern: (Time complexity: O(n))

def same(a=list, b=list):
    if len(a) != len(b):
        return False
    frequencyCounter1 = {}
    frequencyCounter2 = {}
    for val in a:
        frequencyCounter1[val] = frequencyCounter1.get(val, 0) + 1
    for val in b:
        frequencyCounter2[val] = frequencyCounter2.get(val, 0) + 1
    for key in frequencyCounter1:
        if key ** 2 not in frequencyCounter2:
            return False
        if frequencyCounter2[key ** 2] != frequencyCounter1[key]:
            return False
    return True


same([1,2,3], [4,1,9])
same([1,2,3], [1,9])
same([1,2,1], [4,4,1])



# Application of Frequency Counter Pattern
# Q2) Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

def validAnagram(a=str, b=str):
    if len(a) != len(b):
        return False
    lookup = {}
    for i in range(len(a)):
        letter = a[i]
        if letter in lookup:
            lookup[letter] += 1
        else:
            lookup[letter] = 1
    for i in range(len(b)):
        letter = b[i]
        if not lookup.get(letter, 0):
            return False
        else:
            lookup[letter] -= 1
    return True


validAnagram('', '')
validAnagram('aaz', 'zza')
validAnagram('anagram', 'nagaram')
validAnagram("rat","car")
validAnagram('awesome', 'awesom')
validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana')
validAnagram('qwerty', 'qeywrt')
validAnagram('texttwisttime', 'timetwisttext')