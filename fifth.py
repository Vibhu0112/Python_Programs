class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        pivot=0
        for ar in range(len(nums)-1):
            if nums[ar]>nums[ar+1]:
                pivot=ar+1
                break
        nums = nums[pivot:]+nums[0:pivot]
        left=0
        right=len(nums)-1
        while left<=right:
            mid = int((left+right)/2)
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return False