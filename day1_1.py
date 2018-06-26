# 注释以" #" 开头
#调整字体步骤：file->settings->editor->font->更改size
print("hello world")
print("welcome to python")
#定义变量,不需要去声明变量类型,代码结束可以加不加分号都可以
#python中没有double类型，小数同意使用float
#python3.几的版本中，没有long类型，2点几的版本有
num = 10;#整数
str = "我今天很开心，终于可以学python了"#字符串
money = 3000.05#小数
#复数 complex
com = 1-12j;  #实部 ：1， 虚部：-12
#boolean类型
boolFlag = True;
print(num)
print(str)
print(money)
print(com);
print(boolFlag)
#打印多个值，使用逗号分隔
print(num,str)
#打印数据的类型
print(type(num),type(str),type(money),type(com),type(boolFlag))
#快捷键：撤回上一步：ctrl+z     注释和取消注释：ctrl+斜杠,快速换行：shift+enter
#python中的if else 判断
#注意写法：python不使用 {}  ,使用 :,而且要注意缩进（！！！！！）
if(4>5):
    print("4>5")
else:
    print("4<5")
if(False):
    print("give you a kiss")
else:
    print("kick your ass")

