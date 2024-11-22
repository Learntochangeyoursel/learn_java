# 这是一个对python中变量的作用域进行加强了解的实践
def foo():
    global a  # 声明a为全局变量
    a = 200
if __name__ == '__main__':
    a = 100
    print(a)
# 由于无法从主函数中访问foo中a的值，打印的是全局变量a的值 ，利用global将a声明为全局变量后，就可以将a利用print直接打印出来