def func1():
    yield 1
    yield from func2()
    yield 2

def func2():
    yield 3
    yield 4

# 返回了一个生成器
f1 = func1()
for item in f1:
    print(item)


