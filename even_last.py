lst = "".join(input())
n = 0
if len(lst)>0:
    for i in range(0, len(lst), 2):
        print(lst[i])
        n += int(lst[i])
    n *= int(lst[-1])
print(n)
