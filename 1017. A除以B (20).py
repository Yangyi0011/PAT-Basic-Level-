
# 本题要求计算A/B，其中A是不超过1000位的正整数，B是1位正整数。你需要输出商数Q和余数R，使得A = B * Q + R成立。
# 输入格式：
# 输入在1行中依次给出A和B，中间以1空格分隔。
# 输出格式：
# 在1行中依次输出Q和R，中间以1空格分隔。
# 输入样例：
# 123456789050987654321 7
# 输出样例：
# 17636684150141093474 3

list=[int(x)  for x in input().split()]     # 将输入的字符串以空格分割，获取的字符转为int然后存到list中
Q=list[0]//list[1]                          # //：除法运算，只取商，抛弃余数
print(Q,end=' ')
print(list[0] - Q*list[1])                    #用减法去获取余数

#效果同下

# intputStr = str(input())
# inputArr = intputStr.split()
# A = int(inputArr[0])
# B = int(inputArr[1])
# Q = A // B
# R = A - Q*B
# print(Q, end=" ")
# print(R)
