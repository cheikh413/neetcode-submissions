class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = {}

        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            visited[key] = []

        for i, s in enumerate(strs):
            key = "".join(sorted(s))
            visited[key].append(s)
        result = list(visited.values())
        return result
            

        