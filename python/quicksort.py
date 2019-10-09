quicklist = [3,6,1,2,7,2,4,8]


def quick_sort(arr):
    return q_sort(arr,0,len(arr)-1)

def q_sort(arr,left,right):
    if left < right:
        pos = get_pos(arr,left,right)

        q_sort(arr,left, pos-1)
        q_sort(arr, pos+1, right)
    return arr

def get_pos(arr,left,right):
    pos = arr[left]

    while left<right:
        while left < right and arr[right] >= pos:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] <= pos:
            left +=1
        arr[right] = arr[left]

    arr[left] = pos
    return left

print(quick_sort(quicklist))