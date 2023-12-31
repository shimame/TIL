def hanoi(n, src, dist, via):
    if n > 1:
        hanoi(n - 1, src, via, dist)
        print(str(n) + " : " + src + ' -> ' + dist)
        hanoi(n - 1, via, dist, src)
    else:
        print(str(n) + " : " + src + ' -> ' + dist)

n = int(input())
hanoi(n, 'a', 'b', 'c')