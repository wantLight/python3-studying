def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 定义可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# 关键字参数 在函数内部自动组装为一个dict，可传可不传
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)  # kw获得extra的一份拷贝，对kw的改动不会影响到函数外的extra


# 命名关键字参数:限制关键字参数的名字   def person1(name, age, *, city, job):


# 解决递归调用栈溢出的方法是通过尾递归优化(函数返回的时候，调用自身本身,return语句不能包含表达式。)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
