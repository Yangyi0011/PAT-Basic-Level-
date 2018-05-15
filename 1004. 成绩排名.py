
# 读入n名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。
# 输入格式：每个测试输入包含1个测试用例，格式为
#   第1行：正整数n
#   第2行：第1个学生的姓名 学号 成绩
#   第3行：第2个学生的姓名 学号 成绩
#   ... ... ...
#   第n+1行：第n个学生的姓名 学号 成绩
# 其中姓名和学号均为不超过10个字符的字符串，成绩为0到100之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。
# 输出格式：对每个测试用例输出2行，第1行是成绩最高学生的姓名和学号，第2行是成绩最低学生的姓名和学号，字符串间有1空格。
# 输入样例：
# 3
# Joe Math990112 89
# Mike CS991301 100
# Mary EE990830 95
# 输出样例：
# Mike CS991301
# Joe Math990112


# 学生类
class Student:
    """docstring for student"""

    name = ""  # 姓名
    num = ""  # 学号
    score = 0  # 成绩

    # 构造方法
    def __init__(self, name, num, score):
        self.name = name
        self.num = num
        self.score = score

def getMaxMin(studentArray):
    maxStudent = ""
    minStudent = ""

    maxValue = -1
    minValue = 101

    for student in studentArray:
        if student.score > maxValue:
            maxValue = student.score
            maxStudent = student

        if student.score < minValue :
            minValue = student.score
            minStudent = student

    return maxStudent ,minStudent


number = int(input())
students = []

for i in range(number):
    string = str(input())
    name = string[0:string.find(" ")]  # 获取名字
    # print("name:" + name)

    temp = string[len(name) + 1 : len(string)]  # 获取名字之后到字符串
    # print("temp:" + temp)

    num = temp[0:temp.find(" ")]  # 获取学号
    # print("num:" + num)

    sc = temp[temp.find(" ") + 1:len(temp)]  # 获取成绩
    # print("sc:" + sc)

    if len(name) < 11 and len(num) < 11 and (-1) < int(sc) < 101:
        student = Student(name ,num ,int(sc))
        students.append(student)
    # print("student: " + str(student))

maxStudent ,minStudent = getMaxMin(students)

print(maxStudent.name + " " + maxStudent.num)  # 输出成绩最高的学生的名字和学号
print(minStudent.name + " " + minStudent.num)  # 输出成绩最低的学生的名字和学号