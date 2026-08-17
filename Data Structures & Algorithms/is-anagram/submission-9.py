class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       dict1 = {}
       dict2 = {}
       for character in s: 
        if character in dict1:
            dict1[character] += 1
        else:
            dict1[character] = 1
       for character in t: 
        if character in dict2:
            dict2[character] += 1
        else:
            dict2[character] = 1
       return dict1 == dict2 
        