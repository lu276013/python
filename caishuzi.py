import random
n=int(random.random()*50+1)
i=1
while i <= 5:
a=int(input(“请输入数字：”))
if(a < n):
print(“你输入的数小了”)
i = i + 1
elif(a > n):
print(“你输入的数大了”)
i = i + 1
elif(a==n):
print(“恭喜你猜对了”)
break
else:
print(“你已经猜了5次了，本局是你败北”)
break