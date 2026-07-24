class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        for i in range(len(strs)):
            sort = sorted(strs[i])
            a[tuple(sort)].append(strs[i])
        return list(a.values())





