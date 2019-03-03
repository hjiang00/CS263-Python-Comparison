# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Jacob Lee, Steven Bethard, et al
# 2to3
# fixed by Daniele Varrazzo

# Compatible with Cpython,IronPython(may failed,try delete from.. or use pypy)

from __future__ import print_function
import sys, string

def show(seq,
         table=string.maketrans(b'ACBDGHK\nMNSRUTWVYacbdghkmnsrutwvy',
                                b'TGVHCDM\nKNSYAAWBRTGVHCDMKNSYAAWBR')):

   seq = (''.join(seq)).translate(table)[::-1]
   for i in range(0, len(seq), 60):
      print(seq[i:i+60])


def main(din):
   seq = []
   add_line = seq.append
   for line in sys.stdin:
       for i in range(din):
          if line[0] in '>;':
             show(seq)
             print(line, end='')
             del seq[:]
          else:
             add_line(line[:-1])
   show(seq)

main(int(sys.argv[1]))
