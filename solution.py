from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, first_number in enumerate(nums):
            for j, second_number in enumerate(nums[i + 1 :]):
                if first_number + second_number == target:
                    return [i, i + j + 1]
        return []

    def isPalindrome(self, x: int) -> bool:
        return "".join(list(str(x))[::-1]) == str(x)

    def removeDuplicates(self, nums: List[int | str]) -> int:
        """26. Remove Duplicates from Sorted Array

        Args:
            nums (List[int]): an integer array sorted in non-decreasing order

        Returns:
            int: the number of unique elements in nums
        """

        i = len(nums) - 1
        k = 1
        while i > 0:
            if nums[i - 1] == nums[i]:
                del nums[i]
                nums.append("_")
            else:
                k += 1
            i = i - 1
        return k
