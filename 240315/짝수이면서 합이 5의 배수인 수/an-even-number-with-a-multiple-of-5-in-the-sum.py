n = int(input())

if ((n//10) + (n%10)) % 5 ==0 and n %2 ==0:
    print("Yes")
else:
    print("No")