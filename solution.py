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
