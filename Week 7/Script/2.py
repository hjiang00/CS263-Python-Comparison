import sys
#from memory_profiler import profile
import time
from functools import wraps
def fn_timer(function):
  @wraps(function)
  def function_timer(*args, **kwargs):
    t0 = time.time()
    result = function(*args, **kwargs)
    t1 = time.time()
    print ("Total time running %s: %s seconds" %
        (function.func_name, str(t1-t0))
        )
    return result
  return function_timer

def powLF(n):
    if n == 1:
        return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F) >> 1, (L + F) >> 1)
    else:
        return (L, F)

@fn_timer
def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

if __name__ == '__main__':
    time1 = time.clock()
    fib(int(sys.argv[1]))
    time2 = time.clock()
    print time2 - time1
