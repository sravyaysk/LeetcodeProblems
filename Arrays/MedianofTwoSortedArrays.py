'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n))

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000'''

class Solution:

    def findMedian(self, arr):
        if(len(arr)%2 == 0):
            median = (arr[int(len(arr)/2)] + arr[int(len(arr)/2-1)])/2
        else:
            median = arr[int(len(arr)/2)]
        return median

    def findMedianSortedArrays_bruteForce(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        return self.findMedian(nums)

    def findMedianSortedArrays_EfficientMerge(self, nums1, nums2):
        ##traverse the elements in both lists and copy the smaller one into array
        nums = []
        if(len(nums1) == 0):
            nums = nums2
        elif(len(nums2)==0):
            nums = nums1
        else:
            i = 0; j = 0;
            while (i < len(nums1) and j < len(nums2)):
                if(nums1[i] < nums2[j]):
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1
            while (i < len(nums1)):
                nums.append(nums1[i])
                i += 1
            while (j < len(nums2)):
                nums.append(nums2[j])
                j += 1
        return self.findMedian(nums)

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays_bruteForce([], [1]))
    print(Solution().findMedianSortedArrays_EfficientMerge([], [1]))