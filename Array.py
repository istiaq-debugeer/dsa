def subarray_sum(arr,target):
    n = len(arr)
    current_sum=0
    start=0

    for end in range(n):
        print(end)
        current_sum+=arr[end]
        print('c:',current_sum)
        while current_sum>target:
            current_sum-=arr[start]
            print(current_sum)
            start+=1
        if current_sum==target:
            return [start+1,end+1]

arr1 = [1, 2, 3, 7, 5]
target1 = 12
print(subarray_sum(arr1, target1))  

# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target2 = 15
# print(subarray_sum(arr2, target2))  

# arr3 = [5, 3, 4]
# target3 = 2
# print(subarray_sum(arr3, target3))  
