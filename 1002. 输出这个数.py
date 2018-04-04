
# 读入一个自然数n，计算其各位数字之和，用汉语拼音写出和的每一位数字。
# 输入格式：每个测试输入包含1个测试用例，即给出自然数n的值。这里保证n小于10^100。
# 输出格式：在一行内输出n的各位数字之和的每一位，拼音数字间有1 空格，但一行中最后一个拼音数字后没有空格。
# 输入样例：
# 1234567890987654321123456789
# 输出样例：
# yi san wu

number = int(input())
if number < 10**100:
    string = str(number)    #转成字符串

    list = [int(i) for i in string] #转成整型列表
    sum = sum(list)
# print(sum)

res = str(sum)  #将求和结果字符串化
resStr = ""
for i in res:  #取出每个数字并判断
    if i == '0':
        resStr += "ling"
    elif i == '1':
        resStr += "yi"
    elif i == '2':
        resStr += "er"
    elif i == '3':
        resStr += "san"
    elif i == '4':
        resStr += "si"
    elif i == '5':
        resStr += "wu"
    elif i == '6':
        resStr += "liu"
    elif i == '7':
        resStr += "qi"
    elif i == '8':
        resStr += "ba"
    elif i == '9':
        resStr += "jiu"
    resStr += " "

print(resStr[0:len(resStr) - 1])    #去除最后一个空格