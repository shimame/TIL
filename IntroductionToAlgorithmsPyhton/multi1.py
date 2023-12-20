n = 10
for i in range(1, n):
    for j in range(1, n):
        print(str(i) + '*' + str(j) + '=' + str(i * j))
#print文を1回実行するのにかかる時間をcとしたとき、内側と外側のループをかけて、cn^2の時間がかかる。