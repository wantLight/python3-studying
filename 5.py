import pandas as pd
#变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

#Python内建了map()和reduce()函数。
#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
df = pd.read_excel('工作簿1.xlsx')
print(df)
