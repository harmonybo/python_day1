score = 85;
# if elif else 之间是并列关系，当满足括号中的bool条件时，只会执行一个
# if(score>=80):
#     print("give you a kiss")
# elif(score>=70):
#     print("给你一个爱的抱抱")
# else:
#     print("给你一巴掌")

#当分数为85时，会打印两句代码，原因是第一个id和第二个id不是并列关系，会判断两次
if(score>=80):
    print("给你一个亲亲 QaQ")
if(score>=70):
    print("给你一个抱抱o(*￣▽￣*)o")
else:
    print("你可真是个废物 (T_T)")