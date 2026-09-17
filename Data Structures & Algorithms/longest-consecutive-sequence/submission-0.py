class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se=set(nums)
        best=0
        for el in se: 
            if el-1 not in se:
                length=1
                while(el+length)in se:
                    length+=1
                best=max(best,length)
        return best
        