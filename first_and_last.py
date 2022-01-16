from re import I


def first_and_last1(arr, target):
    target_first_last_arr = [-1, -1]
    idx = 0
    arr.sort()
    for i in range(len(arr)):
        if target == arr[i] and idx == 0 :
            target_first_last_arr[0] = i 
            idx += 1
        if target == arr[i] and idx > 0 :
            target_first_last_arr[1] = i 

    return target_first_last_arr

def first_and_last2(arr, target):
    arr.sort()
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]
    start = find_start(arr,target)
    end = find_end(arr, target)
    return [start, end]

def find_start(arr,target):
    if arr[0] == target:
        return 0
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left+right)//2
        if arr[mid] == target and arr[mid -1] < target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_end(arr, target):
    if arr[-1] == target:
        return len(arr) - 1
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right)//2
        if arr[mid] == target and arr[mid + 1] > target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1 


print(first_and_last2([6,5,2,3,4,5,5,7],5))

        