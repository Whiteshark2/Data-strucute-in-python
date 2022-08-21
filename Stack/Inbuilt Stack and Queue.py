import queue



# Inbuilt stack as List
#s = [2,3,4]
##s.append(34)
#print(s.pop())

"""q = queue.Queue
q.put(34)
q.put(2)
print(q.get())"""

p = queue.lifo()
p.put(23)
print(p.get())