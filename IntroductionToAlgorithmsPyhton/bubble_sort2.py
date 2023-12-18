data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

change = True
for i in range(len(data)):
    if not change: #値の交換が行われていない場合終了
        break
    change = False
    for j in range(len(data) - i - 1): #ソート済みでない範囲でループ
        if data[j] > data[j+1]: #隣り合っている左の値が大きい場合
            data[j], data[j+1] = data[j+1], data[j] #値の交換
            change = True #値の交換が発生した
print(data)