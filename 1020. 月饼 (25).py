# 月饼是中国人在中秋佳节时吃的一种传统食品，不同地区有许多不同风味的月饼。现给定所有种类月饼的库存量、总售价、以及市场的最大需求量，请你计算可以获得的最大收益是多少。
#
# 注意：销售时允许取出一部分库存。样例给出的情形是这样的：假如我们有3种月饼，其库存量分别为18、15、10万吨，总售价分别为75、72、45亿元。如果市场的最大需求量只有20万吨，那么我们最大收益策略应该是卖出全部15万吨第2种月饼、以及5万吨第3种月饼，获得 72 + 45/2 = 94.5（亿元）。
#
# 输入格式：
#
# 每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N表示月饼的种类数、以及不超过500（以万吨为单位）的正整数D表示市场最大需求量。随后一行给出N个正数表示每种月饼的库存量（以万吨为单位）；最后一行给出N个正数表示每种月饼的总售价（以亿元为单位）。数字间以空格分隔。
#
# 输出格式：
#
# 对每组测试用例，在一行中输出最大收益，以亿元为单位并精确到小数点后2位。
# 输入样例：
#
# 3 20
# 18 15 10
# 75 72 45
#
# 输出样例：
#
# 94.50

#导入operator包的attrgetter()函数
from operator import itemgetter,attrgetter
from decimal import getcontext, Decimal
class Goods:
    weight = 0.0
    price = 0.0
    unitValue = 0.0

    def __init__(self, weight, price):
        self.weight = float(weight);
        self.price = float(price);
        self.unitValue = self.price / self.weight

    def getWeight(self):
        return self.weight

    def getPrice(self):
        return self.price

    def getUnitValue(self):
        return self.unitValue

    def __str__(self):
        return "Goods[ weight：%f，price：%f，unitValue：%f]" % (self.weight, self.price, self.unitValue)

# 贪心算法核心
def greedy(D, w, p):
    n = len(p);

    # 货物初始化
    goodsList = [];
    for i in range(n):
        goods = Goods(float(w[i]), float(p[i]));
        goodsList.append(goods);
    #逆序排序
    goodsList = sorted(goodsList,key = attrgetter("unitValue"),reverse=True)
    max = 0;
    i   #声明
    for i in range(len(goodsList)):
        if goodsList[i].getWeight() > D:
            break; #重量超出则跳出
        max += goodsList[i].getPrice();
        D -= goodsList[i].getWeight();

    if i < n:
        # 无法全部卖出，则按重量价格比例计算
        ratio = D / goodsList[i].getWeight(); #比例系数
        max += goodsList[i].getPrice() * ratio;
    return max;

# 主程序开始
ND = input()
arr = ND.split(" ")
N = int(arr[0])   #月饼种类
D = int(arr[1])    #市场容纳量
w = []      #每种月饼的库存量
p = []      #每种月饼的总销售额

#初始化
if N <= 1000 and D <= 500:
    W = input()
    P = input()
    w = W.split(" ")
    p = P.split(" ")

    res = greedy(D,w,p);
    res = Decimal(str(res)).quantize(Decimal('0.00'))
    print(res)
    exit(0)