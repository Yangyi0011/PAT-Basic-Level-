#
# 给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：
# A1 = 能被5整除的数字中所有偶数的和；
# A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；
# A3 = 被5除后余2的数字的个数；
# A4 = 被5除后余3的数字的平均数，精确到小数点后1位；
# A5 = 被5除后余4的数字中最大数字。
# 输入格式：
# 每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。
# 输出格式：
# 对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。
# 若其中某一类数字不存在，则在相应位置输出“N”。
# 输入样例1：
# 13 1 2 3 4 5 6 7 8 9 10 20 16 18
# 输出样例1：
# 30 11 2 9.7 9
# 输入样例2：
# 8 1 2 4 5 6 7 9 16
# 输出样例2：
# N 11 2 N 9

def getA1(A1):
    res = ""
    if len(A1) == 0:
        res = "N"
    else:
        sum = 0;
        for a in A1:
            if a % 2 == 0:
                sum += a
        if sum == 0:
            res = "N"
        else:
            res = str(sum)
    return res

def getA2(A2):
    res = ""
    if len(A2) == 0:
        res = " N"
    else:
        # print(A2[0::2])
        temp1 = sum(A2[0::2])           # n1 + n3 + n5 + ....
        temp2 = sum(A2[1::2])*(-1)      # -(n2 + n4 + n6 + ....)
        res = " " + str(temp1 + temp2)
    return res

def getA3(A3):
    res = ""
    if len(A3) == 0:
        res = " N"
    else:
        res = " " + str(len(A3))
    return res

def getA4(A4):
    res = ""
    if len(A4) == 0:
        res = " N"
    else:
        avg = sum(A4)*1.0 / len(A4)
        res = " " + str(round(avg,1))   #round(参数，精度)
    return res

def getA5(A5):
    res = ""
    if len(A5) == 0:
        res = " N"
    else:
        res = " " + str(max(A5))
    return res

#程序开始
string = str(input())
strArr = string.split(" ")
tempArr = strArr[1:]
arr = []
for i in tempArr:
    arr.append(int(i))

A1 = []
A2 = []
A3 = []
A4 = []
A5 = []

for a in arr:
    remainder = a % 5
    if remainder == 0:
        A1.append(a)
    elif remainder == 1:
        A2.append(a)
    elif remainder == 2:
        A3.append(a)
    elif remainder == 3:
        A4.append(a)
    elif remainder == 4:
        A5.append(a)
res = ""
res += getA1(A1)
res += getA2(A2)
res += getA3(A3)
res += getA4(A4)
res += getA5(A5)
print(res)
