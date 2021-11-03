# n = int(input("数字1:") + "【<-数字を入力】")
# m = int(input("数字2:") + "【<-数字を入力】")

n = int(input("数字1:"))
m = int(input("数字2:"))
mn = 0
for i in range(n,m + 1):
    mn += i
print('{0}から{1}までの合計は{2}です'.format(n,m,mn))