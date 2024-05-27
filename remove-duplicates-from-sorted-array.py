from solution import Solution


def main():
    solution = Solution()

    for nums, target in [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([], 0),  # Leere Liste
        ([1, 1, 1, 1, 1], 1),  # Liste mit gleichen Elementen
        ([1, 2, 3, 4, 5], 5),  # Liste ohne Duplikate
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 5),  # Jedes Element ist doppelt
        ([1, 2, 2, 3, 3, 4, 4, 5, 5], 5),  # Erstes Element ist einzigartig, Rest sind Duplikate
    ]:
        result = solution.removeDuplicates(nums)
        print(("✅" if target == result else "❌") + f" for {nums=}")


if __name__ == "__main__":
    main()
