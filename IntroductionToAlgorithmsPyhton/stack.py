#スタックはLIFO(Last In First Out)
stack = []

stack.append(3) #要素を末尾に追加
stack.append(5)
stack.append(2)

temp = stack.pop() #末尾の要素を取り出し、リストから削除
print(temp)

temp = stack.pop()
print(temp)

stack.append(4)

temp = stack.pop()
print(temp)