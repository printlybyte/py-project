# def fun(i, j):
#     return str(j) in str(i)
#
# nums = (1, 1)
# r = 3
# total = 0
# for i in range(3):
#     total += fun(nums, r)
#     p, q = nums
#     nums = (q, p + q)
#
# print("i = "+str(i))
# print("nums = "+str(nums))
# print("total = "+str(total))


num = input("place 1")
N = input("place 2")
if num.isdigit() and N.isdigit():
    for k in range(1, int(N)):
        resu=  k + int(num)
        print(str(k)+"+"+str(num )+"="+str(resu))
else:
    print("Invalid Input")




# A = input("place 1")
# B = input("place 2")
#
#


