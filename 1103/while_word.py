tango = []
while True:
    n = input("単語を入力してください:")
    if n in "":
            print("終了します")
            print("これまでに覚えた単語:" , tango)
            break
    if n in "LIST":
            print("単語リスト:" , tango)
            continue
    if n in tango:
            print("既に登録済みです")
            continue
    else:
            tango.append(n)


# list
#     hyouji
# ----------
#     space
#             itiran
# ----------------------- 
#             tuika
#             sudeni
    