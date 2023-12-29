def count_string(data):
    i = 0
    count = 0
    num = 0
    result = []
    while i < len(data):
        if num == int(data[i]): #一つ前の数と同じ数の場合
            count += 1
        else:
            result.append(count) #一つ前の数と現在の数が違う場合、連続(count)の値を配列に追加する
            count = 1

        if i == len(data) - 1: #配列の最後の要素の場合
            result.append(count)

        if i == 0 & int(data[i]) == 1: #最初の要素の値が1である場合、0にする。
            data[i] = 0
            count += 1
        
        num = int(data[i]) #現在の値をnumに代入する。

        #print("i = " + str(i) + "   data[i] = " + str(data[i]))
        i += 1
    return result

data = "000000111111100111000000001111"
print(count_string(data))