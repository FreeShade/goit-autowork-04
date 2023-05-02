from random import randint


def get_random_password():
    my_list = []
    while True:
        if len(my_list) < 8:
            random_num = randint(40, 126)
            a = chr(random_num)
            my_list.append(a)
        else:
            break

    my_string = "".join(my_list)
    return my_string
