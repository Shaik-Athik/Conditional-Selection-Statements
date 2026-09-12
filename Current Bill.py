n=int(input())
c=0
s=0
if n<=199:
    c=1.20
elif n>=200 and n<400:
    c=1.50
elif n>=400 and n<600:
    c=1.80
else:
    c=2.00
bill=(n*c)
if bill>=400:
    s=(bill*0.15)
else:
    s=100
total=bill+s
print(f"{total:.2f}")
