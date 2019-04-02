import sys

sys.setrecursionlimit(1000000)

def get_pie(times):
    if times <= 0:
        return 0
    else:
        times -= 1
        a = (-1)**(times)
        b = 2*times + 1
        c = a/b
        result = c + get_pie(times)
        # result = ((-1)**(times))/(2*times + 1) + get_pie(times)
        return result


if __name__ == '__main__':
    pie = get_pie(21000)*4
    print(pie)
