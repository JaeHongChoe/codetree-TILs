a = input()
a= list(a)
check=0

for k in range(1,len(a)):
    if a[k] == '0':
        a[k] = '1'
        check=1
        break
if check ==0:
    a[-1] ='0'

ans = "".join(a)

print(int(ans,2))