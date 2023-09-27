def insert_sort(arr):
    for i in range (len(arr)):
        cur_ind=i
        cur=arr[i]
        while cur_ind-1>=0 and arr[cur_ind-1]>cur:
            arr[cur_ind]=arr[cur_ind-1]
            cur_ind-=1
        arr[cur_ind]=cur
    return arr

  