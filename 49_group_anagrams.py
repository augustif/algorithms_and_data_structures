class Solution:
    def group_anagrams(self, strs: list) -> list[list[str]]:
        anagram_map = {}
        result = []
        for word in strs:
            #  this would give an error since the word_sorted would be a list --> python dicts must receive immutable obects as keys
            # word_sorted = sorted(word)
            # anagram_map[word_sorted].append(word)

            word_sorted = tuple(sorted(word))
            if word_sorted not in anagram_map.keys(): #to avoid this check you can use the alternative version below
                anagram_map[word_sorted] = []
            anagram_map[word_sorted].append(word)
        
        result = [elem for elem in anagram_map.values()]
        return result           

## Alternative version
# from collections import defaultdict
# class Solution:
#     def group_anagrams(self, strs: list) -> list[list[str]]:
#         anagram_map = defaultdict(list)
#         result = []
#         for word in strs:
#             #  this would give an error since the word_sorted would be a list --> python dicts must receive immutable obects as keys
#             # word_sorted = sorted(word)
#             # anagram_map[word_sorted].append(word)

#             word_sorted = tuple(sorted(word))
#             anagram_map[word_sorted].append(word)
        
#         result = [elem for elem in anagram_map.values()]
#         return result 

if __name__ == '__main__':
    strs = ['eat', 'ate', 'bat']
    solution = Solution()
    sol = solution.group_anagrams(strs)
    print(sol)