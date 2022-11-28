# 文字列型
fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + 'BANANA'
print(new_fruit)

fruit = """apple
banana
grape
"""
print(fruit)

fruit = 'banana'
print(fruit[2])


#encode, decode =>bytes[]
byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))


#count
msg = 'ABCDEABC'
print(msg.count('ABC'))


#startswith, endswith
print(msg.startswith('ABCD')) #ABCDで始まる文字列だったらTRUEと表示される
print(msg.startswith('ABCE'))

print(msg.endswith('C')) #msgがCでおわってたらTRUE
print(msg.endswith(' ED')) 


#strip(両端), rstrip(右端）, lstrip（左端）　　を削除する

meg = ' ABC '
print(meg)
print(meg.strip())


#upper, lower, swapcase, replace, catitalize
msg = 'abcABC'
msg_u = msg.upper() #大文字
msg_l = msg.lower() #小文字
msg_s = msg.swapcase() #大文字小文字入れ替え
print(msg_u, msg_l, msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'FFF')
print(msg_r)

msg = 'hello world'
print(msg.capitalize())

#文字列の一部取り出し, format, islower, isupper
msg = 'hello, my name is taro'
print(msg[1:6])
print('hello{}'.format('Taro'))
name = 'Jiro'
print(f'hello{name}')
print(f'{name=}')

msg = 'apple'
print(msg.islower())
print(msg.isupper())


#find, index, rfind, rindex
msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))


