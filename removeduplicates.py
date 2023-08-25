print("Enter a list items:- ",end=" ")
arr = list(map(int, input().split()))
print("original list is : "+ str(arr))
res = []
[res.append(x) for x in arr if x not in res]
print ("list after removing duplicates : "+ str(res))