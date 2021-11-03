import time
while True:
    n = int(input("何匹数えますか？:"))
    if(n <= 100):
        m = 0.05
        for i in range(1, n+1, 1):
            time.sleep(m)
            m += 0.01
            print("羊が{0}匹".format(i))
    else:
        print("100までの数字を入力してください")
