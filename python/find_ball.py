import random

# 4 4 4
def first_find_weight(ball_list):
    f1, f2, f3 = ball_list[0:4], ball_list[4:8], ball_list[8:13]
    if f1 == f2:
        return [f3, 1, "f3"] if f1 < f3 else [f3, 0, "f3"]
    elif f1 > f2:
        return [f1, 1, "f1"] if f1 > f3 else [f2, 0, "f2"]
    elif f1 < f2:
        return [f1, 0, "f1"] if f1 < f3 else [f2, 1, "f2"]


# 2 2
def second_find_weight(status_list):
    s1, s2, w, ball_sublist = status_list[0][0:2], status_list[0][2:4], status_list[1], status_list[2]
    # w = 1
    if w:
        return [s1, 1, "s1", ball_sublist] if s1 > s2 else [s2, 1, "s2", ball_sublist]
    else:
        return [s1, 0, "s1", ball_sublist] if s1 < s2 else [s2, 0, "s2", ball_sublist]


def third_find_weight(status_list):
    t1, t2, w, ball_sublist, second_ball_sublist = status_list[0][0:1], status_list[0][1:2], status_list[1], \
                                                   status_list[2], status_list[3]

    # w = 1
    if w:
        return [t1, 1, "t1", ball_sublist, second_ball_sublist] if t1 > t2 else [t2, 1, "t2", ball_sublist,
                                                                                 second_ball_sublist]
    else:
        return [t1, 0, "t1", ball_sublist, second_ball_sublist] if t1 < t2 else [t2, 0, "t2", ball_sublist,
                                                                                 second_ball_sublist]


def parser(status_list):
    w, t, s, f = status_list[-4:]

    f1 = list(range(0, 4))
    f2 = list(range(4, 8))
    f3 = list(range(8, 12))

    f_dict = {'f1': f1, 'f2': f2, 'f3': f3}

    f = f_dict.get(f)

    s_dict = {'s1': f[0:2], 's2': f[2:4]}

    s = s_dict.get(s)

    t_dict = {'t1': s[0], 't2': s[1]}

    t = t_dict.get(t)

    if w:
        print(f"特殊小球是第{t+1}个, 为重")
    else:
        print(f"特殊小球是第{t+1}个, 为轻")


if __name__ == '__main__':
    ball_list = [0 for a in range(1, 13)]
    weight_list = [-1, 1]

    index = random.randint(0, 11)
    weight = weight_list[random.randint(0, 1)]

    ball_list[index] = weight

    first_status_list = first_find_weight(ball_list)
    second_status_list = second_find_weight(first_status_list)
    third_status_list = third_find_weight(second_status_list)
    print("小球列表为", ball_list)
    parser(third_status_list)
