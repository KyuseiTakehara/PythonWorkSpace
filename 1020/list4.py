'''
整数を入力してください６
1~６までの合計: 21 
平均:3.5
'''

n = input("整数を入力してください")
a = range(1,int(n) + 1)
b = sum(a)
c = b/len(a)
print(f"1~{n}までの合計: {b} ")
print(f"平均:{c}")