test_list = [1, 4, 6, 7, 9, 3, 5,45,75,29]
 
print("The original list : " + str(test_list))
 
res = [test_list[i] for i in range(len(test_list)) if i % 2 != 0]

print("The alternate element list is : " + str(res))