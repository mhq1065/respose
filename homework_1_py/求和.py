sumu=0
n=1
u=1/((n+1)*(n+4))
while u>1E-10:
    sumu=sumu+u
    n=n+1
    u=1/((n+1)*(n+4))
sumu=sumu+u
print(sumu)