class Solution:
    def findDuplicates(self, arr):
        seen = set()

        duplicates = []

        for num in arr:
            if num in seen:

                duplicates.append(num)  # Found a duplicate
            else:
                seen.add(num)  # Add first occurrence to set

        return duplicates


arr = [4, 3, 2, 7, 8, 2, 3, 1]
sol = Solution()
print(sol.findDuplicates(arr))  # Output: [2, 3]
