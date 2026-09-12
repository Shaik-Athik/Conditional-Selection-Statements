n=int(input())
if n%2==0 and 1<n<5:
    print("not weird")
elif n%2==0 and 6<n<20:
    print("weird")
elif n%2==0 and n>20:
    print("not weird")
else:
    print("weird")
