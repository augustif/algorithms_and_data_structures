# 'a' 'b'

# A) iterative loop over ransomNote (n) and remove found letters from magazine (m): O(n*m)
    # - to remove letters from magazine the python backend need to store a copy of it because strings are immutable --> space complexity: O(m)

# B) hashmaps: place each magazine letter in a hashmap as separate keys -> O(n)

class SolutionA:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for rl in ransomNote:
            if rl not in magazine:
                return False
            else:
                magazine.replace('rl', '', 1) #replace only first occurrence
        return True

class SolutionB:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hashmap = {letter:0 for letter in magazine}
        for letter in magazine:
            magazine_hashmap[letter] +=1

        for letter in ransomNote:
            if letter in magazine_hashmap:
                if magazine_hashmap[letter]>0:
                    magazine_hashmap[letter]-=1
                    ransomNote = ransomNote[1:]
        
        if len(ransomNote) == 0:
            return True
        else: 
            return False