data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

#ヒープを構成
for i in range(len(data)):
    print("-----------------")
    j = i
    print("i = " + str(i))
    print("(j - 1) // 2 = " +str((j - 1) // 2))
    print("\t   j = " + str(j))
    print(str(data[(j - 1) // 2]) +  " < " + str(data[j]))
    
    while (j > 0) and (data[(j - 1) // 2] < data[j]):

        
        print(str(data[(j - 1) // 2])+" <-> " + str(data[j]))
        data[(j - 1) // 2], data[j] = data[j], data[(j - 1) // 2] #親ノードと子ノードを交換

        
        print(data)

        print("next_j = " + str((j - 1) // 2))
        j = (j - 1) // 2 #親の位置に移動
        print("-----------------")
    print("False: "+str(data[(j - 1) // 2]) +  " < " + str(data[j]))

        
