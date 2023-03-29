class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = nums.count(val)
        while count != 0:
            nums.remove(val)
            count = nums.count(val)