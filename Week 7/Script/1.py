import sys
# from memory_profiler import profile
# from guppy import hpy
# hxx = hpy()
# heap = hxx.heap()
# byrcs = hxx.heap().byrcs;

def powLF(n):
    if n == 1:
        return (1, 1)
    L, F = powLF(n//2)
    L, F = (L**2 + 5*F**2) >> 1, L*F
    if n & 1:
        return ((L + 5*F) >> 1, (L + F) >> 1)
    else:
        return (L, F)

# @profile
def fib(n):
    if n & 1:
        return powLF(n)[1]
    else:
        L, F = powLF(n // 2)
        return L * F

def s():
    for i in range(100000):
        fib(ip)

if __name__ == '__main__':
    ip = int(sys.argv[1])
    import cProfile
    cProfile.run("s()", sort="cumulative")
    # print heap
