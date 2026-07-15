class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counts = [0] * 26 # counter for a to z

            for char in word:
                index = ord(char) - ord("a") # gives index in the alphabet
                counts[index] += 1
            key = tuple(counts) # locks the index; serves as the fingerprint
            groups[key].append(word)

        return list(groups.values())
        