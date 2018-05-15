
# 令Pi表示第i个素数。现任给两个正整数M <= N <= 104，请输出PM到PN的所有素数。
# 输入格式：
# 输入在一行中给出M和N，其间以空格分隔。
# 输出格式：
# 输出从PM到PN的所有素数，每10个数字占1行，其间以空格分隔，但行末不得有多余空格。
# 输入样例：
# 5 27
# 输出样例：
# 11 13 17 19 23 29 31 37 41 43
# 47 53 59 61 67 71 73 79 83 89
# 97 101 103

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

#获取前N个素数
def getPrimes(N):
    primeList = []
    i = 2;
    while(len(primeList) < N):
        if(isPrime(i)):
            primeList.append(i)
        i += 1
    return primeList

string = str(input())
arr = string.split(" ")
M = int(arr[0])
N = int(arr[1])

if M <= N <= math.pow(10,4):
    primeList = getPrimes(N)
    # print(primeList)

    printCnt = 0;
    for i in range(M-1,len(primeList)): #因为下标从0开始，所以要-1
        print(primeList[i],end="")
        printCnt += 1
        if(i != len(primeList) - 1 and printCnt % 10 != 0):
            print(" ",end="")
        if(printCnt % 10 == 0):
            print()
            printCnt = 0;