# python 学习字符串切片(slice)实践作业

# 语法如下：[start:end:step]
# [:] 从开头到结尾提取整个字符串，start 默认值 0 end 默认值 -1，这个操作暂时无用

letter = 'learntochangemyself'
print(letter[:])
# 无效操作
print(letter[3:])
# 从索引为3的字符串中截取子字符串
print(letter[:len(letter)])
# 字符串从头截取至end-1，len(str) 获取字符串的长度，字符串最大索引值等于字符串长度-1
print(letter[1:19])
# 
print(letter[::-1])
# 反串，设置 step 的默认值