data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

#ヒープを構成
for i in range(len(data)):
    j = i
    while (j > 0) and (data[(j - 1) // 2] < data[j]):
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2] #親ノードと子ノードを交換
        j = (j - 1) // 2 #親の位置に移動
    

#ソートを実行
for i in range(len(data), 0, -1):
    #ヒープの先頭と交換
    data[i - 1], data[0] = data[0], data[i - 1]
    j = 0 #ヒープの先頭から開始
    while ((2 * j + 1 < i - 1) and (data[j] < data[2 * j + 1]))\
       or ((2 * j + 2 < i - 1) and (data[j] < data[2 * j + 2])): #左下の方が大きい or 右下の方が大きい
        if ((2 * j + 2 == i - 1) or (data[2 * j + 1] > data[2 * j + 2])): #左下の方が大きい

            #左下と交換
            data[j], data[2 * j + 1] = data[2 * j + 1], data[j]
            #左下に移動
            j = 2 * j + 1
        else: #右の方が大きい
            #右下と交換
            data[j], data[2 * j + 2] = data[2 * j + 2], data[j]
            #右下に移動
            j = 2 * j + 2

print(data)