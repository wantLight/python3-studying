#不换行输出
print("请输入",end="")
#py不能自动进行类型转换
age=input("年龄：")
age=int(age)
#and or not
if age >= 18 or age <= 0:
    print("成年")
elif age == 21:
    print("wsq")
else:
    print("lalalala")
#产生随机数
import random
computer = random.randint(0,100)
i = 1
while i < 10:
    print(i)
    i += 1

i=0
j=5
while i < 5:
    i+=1
    print(" "*(5-j),end="")
    print("*"*j)
    j-=1