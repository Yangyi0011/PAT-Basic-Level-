
# 让我们用字母B来表示“百”、字母S表示“十”，用“12...n”来表示个位数字n（<10），换个格式来输出任一个不超过3位的正整数。例如234应该被输出为BBSSS1234，因为它有2个“百”、3个“十”、以及个位的4。
# 输入格式：每个测试输入包含1个测试用例，给出正整数n（<1000）。
# 输出格式：每个测试用例的输出占一行，用规定的格式输出n。
# 输入样例1：
# 234
# 输出样例1：
# BBSSS1234
# 输入样例2：
# 23
# 输出样例2：
# SS123

n = int(input())
res = ""

if 0 < n < 1000:
    if len(str(n)) == 1:
        for i in range(n):
            res += str(i+1)

    if len(str(n)) == 2:
        si = (int)(n / 10)
        ge = n % 10
        for i in range(si):
            res += "S"
        for i in range(ge):
            res += str(i+1)

    if len(str(n)) == 3:
        bai = (int)(n / 100)        #获取白位
        si = (int)((n % 100) / 10)  #获取十位
        ge = n % 10                 #获取各位
        for i in range(bai):
            res += "B"
        for i in range(si):
            res += "S"
        for i in range(ge):
            res += str(i+1)
    print(res)
