# class solution:
#     def missing_array(self, arr):
#         n = len(arr)

#         total = (n + 1) * (n + 2) // 2

#         sum_of_arr = sum(arr)

#         return total - sum_of_arr


# arr = [1, 2, 4, 6, 3, 7, 5, 8, 6, 10]
# sol = solution()

# print(sol.missing_array(arr))  # 5


# Brute force
class solution:
    def missing_array(self, arr):
        n = len(arr) + 1

        for i in range(1, n + 1):
            print("i", i)
            found = False
            for j in range(n - 1):
                print("j", j)
                if arr[j] == i:
                    found = True
                    break

            if not found:
                return i


arr = [1, 2, 3, 5, 6, 7, 9]
sol = solution()
print(sol.missing_array(arr))  # 4


# brute_force optimization


def missingNumber(self, n, arr):
    arr.sort()

    # Iterate through the array to find the missing number
    for i in range(n - 1):
        if arr[i] != i + 1:
            return i + 1

    # If no number is missing, return n (this line should be logically unreachable in the problem constraints)
    return n
