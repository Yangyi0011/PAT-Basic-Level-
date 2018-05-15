
# 设计函数求一元多项式的导数。（注：xn（n为整数）的一阶导数为n*xn-1。）
# 输入格式：以指数递降方式输入多项式非零项系数和指数（绝对值均为不超过1000的整数）。数字间以空格分隔。
# 输出格式：以与输入相同的格式输出导数多项式非零项的系数和指数。数字间以空格分隔，
# 但结尾不能有多余空格。注意“零多项式”的指数和系数都是0，但是表示为“0 0”。
# 输入样例：
# 3 4 -5 2 6 1 -2 0
# 输出样例：
# 12 3 -10 1 6 0

str_input = str(input()).split(" ")    #获取输入数据
str_res = ""        #结果返回
coefficient = 0     #记录输入的系数
exponential = 0     #记录输入的指数

if len(str_input) > 2:                          #非零多项式
    for i in range(len(str_input)):
        if i % 2 == 0:
            coefficient = int(str_input[i])     #提取系数
        else:
            exponential = int(str_input[i])     #提取指数

        if i % 2 != 0 and exponential != 0:     #将常数项当成常数项之后的0的系数
            newCoe = exponential*coefficient    #得到求导后的系数
            newExp = exponential - 1            #得到求导后的指数

            if str_res != "":
                str_res += " "
            str_res += str(newCoe)          #结果集添加系数

            if newExp != 0:
                str_res += " "
                str_res += str(newExp)      #结果集添加指数，指数为0的不添加
    str_res += " 0"                         #添加多项式等号后的0
else:
    str_res += "0 0"                        #零多项式
print(str_res)




