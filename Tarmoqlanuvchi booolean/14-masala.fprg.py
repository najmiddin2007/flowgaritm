a=int(input())
b=int(input())
c=int(input())
if (a<b<c) or (a<c<b):
    print(a,end=' ')
if (b<a<c) or (b<c<a):
    print(b,end=' ')
if (c<b<a) or (c<a<b):
    print(c,end=' ')
if (a>b>c) or (a>c>b):
    print(a,end=' ')
if (b>a>c) or (b>c>a):
    print(b,end=' ')
if (c>a>b) or (c>b>a):
    print(c,end=' ')
