while True:
    n = str(input("好きな文字を入力してください"))
    if n == "":
            break
    if n.isnumeric():
        print("整数")
    elif n.isalpha():
        print("アルファベット")
    elif n.isalnum():
        print("アルファベットと数字")
    else:
        print("その他")