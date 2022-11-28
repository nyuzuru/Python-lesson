#remove, pop, count, index

list_a = [0,1,1,2,2,2,3,3,3,3,4,]
list_b = list_a[:3]


list_a.remove(3)
print(list_a)

value = list_a.pop()
print(list_a, value)
print(list_a.count(0))
print(list_a.index(3))# 3が初めて登場するインデックス番号を表示

#copy
print(list_a)
list_b = list_a.copy()
list_b[0] = 'AAAAA'
print(list_a)


#sort, reverse
list_a = ['banana', 'apple', 'lemon', 'grape']
print(list_a)
# list_a.sort()
list_a = sorted(list_a)
list_a.reverse()
print(list_a)
