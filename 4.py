#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g = fib(6)
#想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
        print('Generator return value:', e.value)
        break

def triangles():
    row = [1]
    while True:
        yield (row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
