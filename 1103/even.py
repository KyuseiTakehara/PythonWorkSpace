# n = 2
# print("偶数一覧")
# print("=>" , end=" ")
# while True:
#     if (n < 99):
#         print(n , end="")
#         print("," , end=" ")
#         n = n + 2
#     else:
#         break

print("偶数一覧=>",end='')
for i in range(1,100):
    if i % 2 == 0:
        print(i, end=', ')
print()

# result = []
# for i in range(1,100):
#     if i % 2 == 0:
#         result.append(i)
# print(f'偶数一覧=>{result}')