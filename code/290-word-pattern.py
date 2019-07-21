#290. Word Pattern






class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dic={}
        str = str.split()
        if len(pattern)!=len(str):
            return False
        for i in range(len(pattern)):
            word = str[i]
            if pattern[i] in dic.keys():
                if dic[pattern[i]]!=word:
                    return False
            else:
                if word in dic.values():#avoid abba--dog dog dog dog
                    return False
                dic[pattern[i]] = word
        return True