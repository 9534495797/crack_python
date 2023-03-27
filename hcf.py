def hcf(a,b):
    if a>b:
        small=a
    else:
        small=a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
print(hcf(10,20))