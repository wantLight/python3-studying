from collections import Iterable
import os # 导入os模块，模块的概念后面讲到
#指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[1:3])
#倒数第一个元素的索引是-1
print(L[-2:-1])
#所有数，每2个取一个：
print(L[0:5:2])

#使用for循环时，只要作用于一个可迭代对象
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k+":"+str(v))
print(isinstance('abc', Iterable)) # str是否可迭代

#enumerate函数可以把一个list变成索引-元素对 for循环本质上就是通过不断调用next()函数实现的
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

def findMinAndMax(L):
    if(L==[]):
        return (None, None)
    min=max=L[0]
    for i in L:
        if(i>max):
            max = i
        elif(i<min):
            min = i
    return (min,max)

if findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')

#列表生成式 [x * x for x in range(1, 11) if x % 2 == 0]
print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
