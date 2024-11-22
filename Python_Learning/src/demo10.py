# python 元组的使用
# 定义方式 name = ()

tuple1 = ('张三',38,True,'四川成都')
print(tuple1)
# 定义元组

print(type(tuple1))
# 查看元组的数据类型

print(tuple1[0])
# 获取元组中第一个元素

# 元组相当于常量，无法在定义后单独对元组中的单一数据进行更改，但是可以直接对整个元组进行更改。
# tuple1[0] = '王五' 会报错
tuple1 = ("赵四",30,False,'贵州贵阳')
print(tuple1)

# 可以将元组转换为链表
list1 = list(tuple1)

#

