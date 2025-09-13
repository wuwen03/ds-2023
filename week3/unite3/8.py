import random,time
arr1=[random.randint(0,10000000) for i in range(100)]
arr2=[random.randint(0,10000000) for i in range(1000)]
arr3=[random.randint(0,10000000) for i in range(10000)]
arr4=[random.randint(0,10000000) for i in range(100000)]
arr5=[random.randint(0,10000000) for i in range(1000000)]



def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr



def merge(s1,s2,s):
    i = j = 0
    while i+j<len(s):
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    merge_sort(s1)
    merge_sort(s2)
    merge(s1,s2,s)


def get_time(fun,arg):
    start=time.perf_counter()
    fun(arg)
    end=time.perf_counter()
    return (end-start)*1000

print("选择排序：")
temp=arr1.copy()
print("100:",get_time(selection_sort,temp),"ms")
temp=arr2.copy()
print("1000:",get_time(selection_sort,temp),"ms")
temp=arr3.copy()
print("10000:",get_time(selection_sort,temp),"ms")
# temp=arr4.copy()
# print("100000:",get_time(selection_sort,temp),"ms")
# temp=arr5.copy()
# print("1000000:",get_time(selection_sort,temp),"ms")


print("归并排序：")
temp=arr1.copy()
print("100:",get_time(merge_sort,temp),"ms")
temp=arr2.copy()
print("1000:",get_time(merge_sort,temp),"ms")
temp=arr3.copy()
print("10000",get_time(merge_sort,temp),"ms")
temp=arr4.copy()
print("100000",get_time(merge_sort,temp),"ms")
temp=arr5.copy()
print("1000000",get_time(merge_sort,temp),"ms")


#相同算法，规模越大排序越慢
#相同规模的情况下，归并排序的消耗的时间优于选择排序
#归并排序的时间复杂度优于选择排序