from solution import Solution


def main():
    solution = Solution()

    for nums, target in [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
    ]:
        result = solution.twoSum(nums, target)
        print(result)


if __name__ == "__main__":
    main()
