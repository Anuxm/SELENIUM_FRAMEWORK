arr=[1,9,8,7,6]
# arr.reverse()
# print(arr)
print(k)
first=arr[0]
last=arr[-1]
for i in arr:
    arr[first],arr[last]=arr[last],arr[first]
    
    
