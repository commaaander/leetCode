from solution import Solution


def main():
    solution = Solution()

    for nums, target in [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ]:
        result = solution.removeDuplicates(nums)
        print(("✅" if target == result else "❌") + f" for {nums=}")


if __name__ == "__main__":
    main()
