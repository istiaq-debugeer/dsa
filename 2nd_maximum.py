def second_max(nums):
    first_max = float("-inf")
    second_max = float("-inf")

    for num in nums:
        if num > first_max:
            second_max = first_max  # Update second max before changing first max
            first_max = num
        elif first_max > num > second_max:  # Ensure it's not equal to first_max
            second_max = num

    return (
        second_max if second_max != float("-inf") else None
    )  # Handle case where no 2nd max exists


# Example usage:
nums = [10, 20, 5, 8, 15]
print(second_max(nums))  # Output: 15
