class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for n in nums:
            di[n]=0
        for n in nums:
            di[n]+=1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for key,value in di.items():
            bucket[value].append(key)
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result