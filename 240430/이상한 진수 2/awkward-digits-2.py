a = input()
a= list(a)
# print(int(a,2))

for k in range(1,len(a)):
    if a[k] == '0':
        a[k] = '1'
        break
    

ans = "".join(a)

print(int(ans,2))