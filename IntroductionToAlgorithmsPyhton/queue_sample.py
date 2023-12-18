#キューはFIFO(First In First Out)
import queue

q = queue.Queue()

q.put(3) #キューに追加
q.put(5)
q.put(2)

temp = q.get() #キューから取り出す
print(temp)

temp = q.get()
print(temp)

q.put(4)

temp = q.get()
print(temp)