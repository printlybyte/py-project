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


# num = input("place 1")
# N = input("place 2")
# if num.isdigit() and N.isdigit():
#     for k in range(1, int(N)):
#         resu=  k + int(num)
#         print(str(k)+"+"+str(num )+"="+str(resu))
# else:
#     print("Invalid Input")


# A = input("place 1")
# B = input("place 2")
#
#
import ast;
class Test():
    def __init__(self):
        pass
    def get_frient_dict(self, frients):
        frientsAll = []
        for k in frients:
            frientsAll.append(k[0])
            frientsAll.append(k[1])
        scheckAll = {}
        for k in set(frientsAll):
            temp = []
            for k1 in frients:
                if (k == k1[0]):
                    temp.append(k1[1])
                elif (k == k1[1]):
                    temp.append(k1[0])
                else:
                    pass
            scheckAll[k] = temp
        print(scheckAll)

if __name__ == "__main__":
    while True:
        frients = input("请输入数据")
        # p1=ast.literal_eval("[('kim', 'sandy'), ('alex', 'sandy'), ('kim', 'alex'), ('kim', 'glenn')]")
        p1=ast.literal_eval(frients)
        t = Test()
        t.get_frient_dict(p1)
