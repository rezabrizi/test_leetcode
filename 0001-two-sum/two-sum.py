class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        for p1 in range(len(nums)-1): 
            for p2 in range(p1+1, len(nums)):
                num1 = nums[p1] 
                num2 = nums[p2]
                if num1+num2 == target:
                    return [p1, p2]
        return -1

        