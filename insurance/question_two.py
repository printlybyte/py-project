import ast;


class Test():
    def __init__(self):
        pass
    """第二题"""
    def friend_besties(self, arr, ids):
        result = []
        for k, v in arr.items():
            for k1 in v:
                if k1 == ids:
                    result.append(k)
                    continue
        return result
    """第三题"""
    def friend_second_besties(self, arr, ids):
        result = []
        resultx = []
        rks = []
        al = arr[ids]
        for kc in al:
            rks.append(kc)
        rks.append(ids)
        for k in al:
            for ks in arr[k]:
                result.append(ks)
            resultx.append(k)
        if len(rks) == 1:
            result.remove(ids)
            return list(result)
        else:
            kcr=list(set(result + rks))
            for kc in rks:
                kcr.remove(kc)
            return kcr




if __name__ == "__main__":
    while True:
        rs = input("请输入数据")
        rsa = ast.literal_eval(rs)
        t = Test()
        print(t.friend_second_besties(rsa[1], rsa[0]))


# 'glenn', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}

# 'kim', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}


# frients = input("请输入数据")
# # p1=ast.literal_eval("[('kim', 'sandy'), ('alex', 'sandy'), ('kim', 'alex'), ('kim', 'glenn')]")
# p1=ast.literal_eval(frients)
# t = Test()
#     # t.get_frient_dict(p1)
# print(p1)


# fs=('kim', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}})
# 'kim', {'kim': {'sandy', 'alex', 'glenn'}, 'sandy': {'kim', 'alex'}, 'alex': {'kim', 'sandy'}, 'glenn': {'kim'}}
