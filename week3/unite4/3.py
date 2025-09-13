import random
def insert_sort(arr):
    for i in range (len(arr)):
        cur_ind=i
        cur=arr[i]
        while cur_ind-1>=0 and arr[cur_ind-1]>cur:
            arr[cur_ind]=arr[cur_ind-1]
            cur_ind-=1
        arr[cur_ind]=cur
    return arr

arr=[random.randint(0,20) for i in range(10)]
print("未排序：",arr)
print("排序后：",insert_sort(arr))