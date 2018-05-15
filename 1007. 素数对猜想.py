
# 让我们定义 dn 为：dn = pn+1 - pn，其中 pi 是第i个素数。显然有 d1=1 且对于n>1有 dn 是偶数。“素数对猜想”认为“存在无穷多对相邻且差为2的素数”。
# 现给定任意正整数N (< 10^5)，请计算不超过N的满足猜想的素数对的个数。
# 输入格式：每个测试输入包含1个测试用例，给出正整数N。
# 输出格式：每个测试用例的输出占一行，不超过N的满足猜想的素数对的个数。
# 输入样例：
# 20
# 输出样例：
# 4

import math
#判断一个数是否是素数
def isPrime(N):
    if N <= 1:
        return False
    elif N == 2:
        return True
    else:
        for n in range(2, int(math.sqrt(N)) + 1):
            if N % n == 0:      #不是素数
                return False
    return True

#获取N以内的所有素数（包含N）
def getPrimes(N):
    primeList = []
    for n in range(2,N + 1):
         if isPrime(n):      #是素数
            primeList.append(n)
    return primeList

number = int(input())

if number < 10 ** 5:
    # primList = getPrimes(number)
    primList = filter(isPrim,range(1,number+1))
    # print(primList)   #获取不超过number的所有素数列表

    cnt = 0     #记录符合题意的素数对个数
    proPrim = 2 #记录上一个素数
    for prim in primList:
        if prim - proPrim == 2:
            cnt += 1;

        # print("上一个：" + str(proPrim))
        # print("当前：" + str(prim))
        proPrim = prim
    # print("素数对的个数：" + str(cnt))
    print(cnt)