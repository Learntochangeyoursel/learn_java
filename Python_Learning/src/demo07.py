# python 中转义字符\的作用

# 需要在 python中打印出引号，需要采用转义字符，\后加一个八进制后十六进制的数表示一个字符
str1 = '\'hello world\''
str2 = '\u5f20\u4e09'
str3 = r'\'hello world\''
# 尝试过去掉转义字符，无法打印出单引号，故此 r 法则无法将单引号直接打印出来，但是可以将特殊转义字符不在转义，如\d、\n
print(str1)
print(str2)
print(str3)