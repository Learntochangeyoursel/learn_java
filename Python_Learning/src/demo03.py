# 这是一个熟悉方法/函数调用的课堂练习
from random import randint

'''摇色子'''
def rollDice (n=0) :
    total = 0
    for _ in range(n) :
        total += randint(1 ,6)
    return  total

'''三数相加'''
def add (a=0,b=0,c=0):
    return a+b+c

'''了解何为形参'''
# 形式参数(formal parameter)在使用是数据类型在python中是链表
def learnFormalParameter(*args):
    # 在此处打印*args
    print(args)
    for i in args:
        print(i)
# main 方法在模块中调用方法时 __name__ ==  '__main__' 其余模块调用时是源码的项目名，此处为demo03
if __name__ == '__main__':
    print(rollDice(2))
    print(add(1,2,2))
    learnFormalParameter(1,2,1,2,3)