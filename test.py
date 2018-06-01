class A:
    meth=5

    def wei(self):
        print(self.meth)

    @classmethod
    def hao(cls):
        print(A.meth)
    @staticmethod
    def jin():
        print("iiii")

# 可以直接调用A中的一些非方法
# a=A()
# print(a.meth)
#
# a=A()
# A.hao()

