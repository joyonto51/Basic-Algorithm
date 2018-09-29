a,b,c = map(int, input().split(' '))
D = (b*b) - 4*a*c

if D >= 0:
    r1 = (-b + D**(1/2)) / (2*a)
    r2 = (-b - D**(1/2)) / (2*a)
    print("root_1 = {}, root_2 = {}".format(r1,r2))

else:
    rp = b / (2*a)
    ip = ((-D)**(1/2)) / (2*a)
    print("real part = {}, imaginary part = {}".format(rp,ip))