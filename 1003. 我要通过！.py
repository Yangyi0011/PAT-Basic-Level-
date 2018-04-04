# 得到“答案正确”的条件是：
# 1. 字符串中必须仅有P, A, T这三种字符，不可以包含其它字符；
# 2. 任意形如 xPATx 的字符串都可以获得“答案正确”，其中 x 或者是空字符串，或者是仅由字母 A 组成的字符串；
# 3. 如果 aPbTc 是正确的，那么 aPbATca 也是正确的，其中 a, b, c 均或者是空字符串，或者是仅由字母 A 组成的字符串。
# 现在就请你为PAT写一个自动裁判程序，判定哪些字符串是可以获得“答案正确”的。
# 输入格式： 每个测试输入包含1个测试用例。第1行给出一个自然数n (<10)，是需要检测的字符串个数。接下来每个字符串占一行，字符串长度不超过100，且不包含空格。
# 输出格式：每个字符串的检测结果占一行，如果该字符串可以获得“答案正确”，则输出YES，否则输出NO。
# 输入样例：
# 8
# PAT
# PAAT
# AAPATAA
# AAPAATAAAA
# xPATx
# PT
# Whatever
# APAAATAA
#
# 输出样例：
# YES
# YES
# YES
# YES
# NO
# NO
# NO
# NO

#解析：
# 1.字符串中的字符只能含有“PAT”三种字符
# 2.xPATx都能通过，x指的是同一字符！同一字符！同一字符！
# 3.aPbTc 是正确的，那么 aPbATca 也是正确的。即原始为PAT，PT之间每多加一个A，T后面多加一个a，同a*b=c
# 4.其中x, a, b, c 均或者是空字符串，或者是仅由字母 A 组成的字符串。即P、T只能出现一次

#判断是否通过的函数
def isPat(string):

    #P和T只能出现一次
    if string.count('P') != 1 or string.count('T') != 1:
        return False
    else:
        for char in string:
            #字符串中的字符只能含有“PAT”三种字符
            if char != 'P' and char != 'A' and char != 'T':
                return False

        #PT之间至少有一个A
        if (string.find('T') - string.find('P')) < 2:
            return False
        #xPATx都能通过
        if  (string.find('T') - string.find('P')) == 2 and string.find("P") == len(string) - 1 - string.find("T"):
            return True

        # a*b=c能通过,a、b、c均值字符串a、b、c中'A'的个数
        a = string.find("P")
        b = string.find("T") - a - 1 #除去一个占位的P
        c = len(string) - a - b - 2  #除去一个占位的P和一个T
        if a * b == c:
            return True

cnt = int(input())  #即将输入字符串的个数

if cnt < 10:
    strList = []   #创建一个空列表
    for i in range(cnt):
        string = str(input())

        #字符串的长度不能大于100且不能包含空格
        if len(string) < 101 and string.find(" ") == -1:
            strList.append(string) #将符合的字符串放入列表中

    #逐一判断输入的字符串是否通过
    for i in range(len(strList)):
        if isPat(strList[i]):
            print("YES")
        else:
            print("NO")
