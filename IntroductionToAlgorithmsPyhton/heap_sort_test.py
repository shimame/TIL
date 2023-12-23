data = [[15, 13, 11, 8, 9, 4, 5, 2, 7, 6]]
for i in range(len(data), 0, -1):
    #ヒープの先頭と交換
    print("i = " + str(i))
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0 #ヒープの先頭から開始
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1]))\
    or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])): #左下の方が大きい or 右下の方が大きい
        print("j = " + str(j))
        if ((2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2])): #左下の方が大きい

            #左下と交換
            print("data[j] = " + str(data[j]))
            print("data[2 * j + 1] = " + str(data[2 * j + 1]))
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            #左下に移動
            j = 2 * j + 1
        else: #右の方が大きい
            #右下と交換
            print("data[j] = " + str(data[j]))
            print("data[2 * j + 2] = " + str(data[2 * j + 2]))
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            #右下に移動
            j = 2 * j + 2
        print("------------while_end")
    print("------------for_end")