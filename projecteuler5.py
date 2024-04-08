import sympy
a=1
for i in range(2,21):
    if sympy.isprime(i):
        a*=i

n=a
while True:
    for i in range(2,21):
        if n%i!=0:
            break
    else:
        print(n)
        break
    n+=a
