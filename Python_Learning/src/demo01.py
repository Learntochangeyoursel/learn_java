#这是一个测试input方法和了解格式化输出的python代码
#运行环境python3.10.0，pycharm2024.1
a = int(input("请输入一个数"))
b = int(input('请输入一个数'))
print(type(a))
print(type(b))
# input 获得控制台输入的数是字符串类型的，需要强制转换为int类型，防止进行四则运算时出错

print('%d + %d = %d' %(a,b,a+b))    #加法
#用占位符输出时，占位符要在引号范围内，对应的变量需要用逗号隔开
print('%d - %d = %d' %(a, b, a - b))    #减法
print('%d * %d = %d' %(a, b, a * b))    #乘法
print('%d / %d = %d' %(a, b, a / b))    #除法
print('%d // %d = %d' %(a, b, a // b))  #去商
print('%d %% %d = %d' %(a, b, a % b))   #取余 %%占位符表示% 转义字符无用
print('%d ** %d = %d' %(a, b, a ** b))  #指数运算
