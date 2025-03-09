# Center aligning a right angled triangle of numbers. the limit will be given for the base level. and from that, a pyramid had to made.


def print_pyramid(n):
    # Upper half (Right-angled triangle)
    for i in range(1, n + 1):
        numbers = " ".join(str(num) for num in range(1, i + 1))
        print(numbers.center(n * 2))  # Center align

    # Lower half (Inverted Right-angled triangle)
    for i in range(n - 1, 0, -1):
        numbers = " ".join(str(num) for num in range(1, i + 1))
        print(numbers.center(n * 2))  # Center align


# Example usage
limit = int(input("Enter the base level limit: "))
print_pyramid(limit)
