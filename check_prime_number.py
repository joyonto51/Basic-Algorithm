n = int(input())
flag = 1
i = 2

while(i<(n/2)):

    if n%i == 0:
        flag = 0
        break

    i+=1

if flag==0:
    print("{} is not a prime number".format(n))
else:
    print("{} is a prime number".format(n))