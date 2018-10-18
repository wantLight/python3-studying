# 列表list: 取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates.pop(1))

#元组tuple: 一旦初始化就不能修改   指向的这个list本身是可变的
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]