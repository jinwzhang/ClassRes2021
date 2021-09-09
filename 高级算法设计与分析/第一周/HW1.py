#更正课后作业：给出课件中组合生成算法的时间递归式，并尝试求解此式，给出时间复杂性的大O表示。


L = [i for i in range(10)]


def sub_sets(a, b, idx, new):
    if idx == len(a):
        new.append(b)
    else:
        c = b[:]  # 不选择a的
        b.append(a[idx])  # 选择a的
        sub_sets(a, b, idx + 1, new)
        sub_sets(a, c, idx + 1, new)


def main():
    a = [i for i in range(5)]  # 指定n集合
    b = []
    new = []
    sub_sets(a, b, 0, new)
    for lst in new:
        if len(lst) == 3:  # 指定m大小
            print(lst)


main()
