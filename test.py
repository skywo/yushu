# class A:
#     meth=5
#
#     def wei(self):
#         print(self.meth)
#
#     @classmethod
#     def hao(cls):
#         print(A.meth)
#     @staticmethod
#     def jin():
#         print("iiii")

# 可以直接调用A中的一些非方法
# a=A()
# print(a.meth)
#
# a=A()
# A.hao()
#
# class lei:
#     mmp=1
#     def __init__(self):
#         self.nub=1
#
# a=lei
#
# print(a.mmp)

# python语音中离线应用，单元测试收到请求后并不会帮你推入应用上下文入栈，而是要手动
from flask import Flask,current_app

app=Flask(__name__)

a=current_app
d=current_app.config["DEBUG"]
