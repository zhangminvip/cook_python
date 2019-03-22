#coding:utf-8

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


grades = []

while True:
    grade_str = input('请输入学生成绩, 输入-1退出\n')
    if grade_str == '-1':
        break
    elif is_number(grade_str):
        grade = int(grade_str)
    else:
        print('请输入整数\n')
        continue
    grades.append(grade)

grades.sort()
count = sum(grades)
average = count/len(grades)
num = 0
for i in grades:
    if i < average:
        num += 1

print('总成绩为%d, 平均成绩为%.2d, 低于平均成绩的人数%d\n' %(count, average, num))
print('排列后到成绩列表为',grades)

