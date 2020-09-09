'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.'''

class Solution:
    def searchNum(self, arr, x, ind):
        for i in range(0,len(arr)):
            if(arr[i] == x and i != ind):
                return i
        return None

    def twoSum_bruteforce(self, nums, target):
        ##Runtime: 5992 ms, faster than 8.75% of Python3 online submissions
        ##Memory Usage: 14.9 MB, less than 84.06% of Python3 online submissions
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
        return None

    def twoSum_searchOtherNumber(self, nums, target):
        ##Runtime: 5160 ms, faster than 16.98% of Python3 online submissions
        ##Memory Usage: 14.9 MB, less than 79.81% of Python3 online submissions
        for i in range(0,len(nums)):
            other_num = target - nums[i]
            j = self.searchNum(nums, other_num, i) #This can be linear or binary search
            if(j is not None):
                return [i,j]
        return None

    def twoSum_useDict(self, nums, target):
        ##Runtime: 52 ms, faster than 72.87% of Python3 online submissions
        ##Memory Usage: 15.4 MB, less than 20.45% of Python3 online submissions
        d = {}
        for ind, num in enumerate(nums):
            other_num = target - num
            j = d.get(num,None)
            if(j is None):
                d[other_num] = ind
            else:
                return [ind,j]

if __name__ == "__main__":
    print(Solution().twoSum_bruteforce([2, 7, 11, 15], 9))
    print(Solution().twoSum_searchOtherNumber([3, 2, 4], 6))
    print(Solution().twoSum_useDict([3,3],6))