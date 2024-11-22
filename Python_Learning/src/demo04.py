# 探究python中变量作用域实操

def foo ():
    b = 'hello world'
    # python 中是允许在函数中创建函数的
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    bar() # 在foo 中调用函数 bar()
    # print(c) NameError: name 'b' is not defined
if __name__ == '__main__' :
    a = 10 # 全局变量
    foo()
    # print(b) #NameError: name 'b' is not defined


# 由运行结果可知，a为全局变量，b为函数foo中的局部变量，c为函数foo中函数bar的局部变量，代码的运行逻辑为：
# 定义一个全局变量 a
# 调用函数 foo() 将 hello world赋值给b
# 调用foo.bar 将True赋值给c，并将a、b、c、给打印出来
# 第一个错误是在代码运行的途中，企图在主函数中将函数foo中的b打印出来
# 第二个错误是企图在foo中将foo中bar里的c打印出来