class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        comparison_list=list(set(nums))
        return len(comparison_list)!=len(nums)
        