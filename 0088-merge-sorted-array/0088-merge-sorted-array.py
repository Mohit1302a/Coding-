class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i, num in zip(range(m, m + n), nums2):
            nums1[i] = num

        nums1.sort()