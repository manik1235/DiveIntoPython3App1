
from DiveIn7_3Support import Fib

fib = Fib(100)
print(fib)
print(fib.__class__)
print(fib.__doc__)

for n in Fib(1000):
    print(n, end=' ')
