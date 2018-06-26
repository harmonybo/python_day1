str = "abcdef";
#可以根据下标来对字符串的某个字符进行取值，下标从0开始，当长度超出时，会报下标越界异常
#python下标可以为负，-1为下标时，获取的是字符串的最后一个字符
#最后一个字符的下标：-1  ，长度减一
firstChar = str[-2];
num = str[len(str)-1]
#len(str)  :获得字符串的长度
print(firstChar,len(str),num)
#"\n"换行
print("床前明月光，\n疑是地上霜")