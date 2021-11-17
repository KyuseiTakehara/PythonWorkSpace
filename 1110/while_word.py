import os
data = 'word.txt'
if os.path.isfile(data):
        with open(data) as f:
                tango = [word.strip() for word in f]
else:
        tango = []

while True:
    n = input("単語を入力してください:") #tangoに入力値を格納
    if n in "":
        #     print("終了します")
        #     print("これまでに覚えた単語:" , tango)
            break
    if n in "LIST": #LISTの場合
            print("単語リスト:" , tango)
            continue
    if n in tango:
            print("既に登録済みです")
            continue
    else:
            tango.append(n)

print("終了します")
print("これまでに覚えた単語:" , tango)

with open(data,'w') as f:
        for word in tango:
                f.write(f'{word}\n')
# list
#     hyouji
# ----------
#     space
#             itiran
# ----------------------- 
#             tuika
#             sudeni
    