fruits = ['バナナ','リンゴ','オレンジ']

while True:
    aa = input("果物をカタカナで入力してください：")
    if aa == '':
        break
    if aa in fruits:
        print(aa + "は、知っています！")
    else:
        print(aa + "は知りませんでした。覚えておきます。")
        fruits.append(aa)

print('知っている果物')
print(fruits)