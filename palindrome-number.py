from solution import Solution


def main():
    solution = Solution()

    for num, target in [
        (121, True),
        (-121, False),
        (10, False),
        (12321, True),  # Palindromzahl
        (12345, False),  # Nicht-Palindromzahl
        (0, True),  # Null ist ein Palindrom
        (11, True),  # Zweistellige Palindromzahl
        (-11, False),  # Negative Zahlen sind keine Palindrome
        (1221, True),  # Vierstellige Palindromzahl
        (123321, True),  # Sechsstellige Palindromzahl
    ]:
        result = solution.isPalindrome(num)
        print(("✅" if target == result else "❌") + f" for {num=}")


if __name__ == "__main__":
    main()
