def kth_largest1(arr,k):
    if k > len(arr):
        return None
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

def kth_largest2(arr,k):
    if k > len(arr):
        return None
    n = len(arr)
    arr.sort()
    return(arr[n - k])

print(kth_largest2([4,2,8,9,5,6,7],2))