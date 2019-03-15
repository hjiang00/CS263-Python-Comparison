# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
# contributed by Joseph LaFata

# Compatible with Jython,IronPython,PyPy

from sys import argv

try:
    N = int(argv[1])
except:
    N = 100

i = k = ns = 0
k1 = 1
n,a,d,t,u = (1,0,1,0,0)
while(1):
    k = 1 + k
    t = n<<1
    n = k * n
    a = t + a
    k1 = 2 + k1
    a = k1 * a
    d = k1 * d
    if a >= n:
        t,u = divmod(n*3 +a,d)
        u = n + u
        if d > u:
            ns = ns*10 + t
            i = 1 + i
            if i % 10 == 0:
                #print ('%010d\t:%d' % (ns, i))
                ns = 0
            if i >= N:
                break
            a = a - d*t
            a = 10 * a
            n = 10 * n
k = 0
k += n
print "this is n ", k
print "this is d ", d
