# 変数の応用

animal = 'dog'
動物 = 'cat'
print(動物)


# 定数

LEGAL_AGE = 20
age = 18

if age < LEGAL_AGE: # age が20より小さい時に処理を実行
    print('未成年')
else:
    print('成人')
    
    
# format文
print(f'age = {age}') # python3.6以降
print(f'{age = }') # python3.8以降
