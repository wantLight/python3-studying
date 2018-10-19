int()
float()
str()
bool()
# 列表list: 取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates.pop(1))

#元组tuple: 一旦初始化就不能修改   指向的这个list本身是可变的
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print(x)
#字典dict: 查找和插入的速度极快，不会随着key的增加而变慢；查找和插入的速度极快，不会随着key的增加而变慢；
# dict的key必须是不可变对象。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85,'test':classmates}
print(d)
#set也是一组key的集合，但不存储value
s = set([1, 2, 3])
