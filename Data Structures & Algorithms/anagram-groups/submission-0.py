class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            # Sort characters to create a canonical key
            key = "".join(sorted(s))

            # Group strings with the same sorted key
            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())