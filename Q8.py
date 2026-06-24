list = [1,2,3,2,1,]


copy_list1 = list.copy()
copy_list1.reverse()

if(copy_list1 == list):
    print("Palindrome")
else:
    print("NOT Palindrome")