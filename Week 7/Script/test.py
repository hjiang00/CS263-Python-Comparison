import os
import psutil
import subprocess
import time

mem_use = 0
t = time.time()
PERCPU_start=psutil.cpu_times(percpu=True)

p = subprocess.Popen('pypy 3.py 100', shell = True, creationflags =0)
#p = subprocess.Popen('python 3.py 100', shell = True, creationflags =0)
pt = subprocess.Popen('time -p pypy 3.py 100', shell = True, creationflags =0)
while p.poll() is None:
	try:
		cpu_time = psutil.Process(p.pid).cpu_times()
		mem_use = max(psutil.Process(p.pid).memory_info().rss, mem_use)
	except:
		break

print 'CPU time: ', cpu_time.user + cpu_time.system
print 'memory usage: ', str(round(mem_use / 1024, 0)) + ' KB'
print 'Elapsed time: ', time.time() - t

PERCPU_exit=psutil.cpu_times(percpu = True)
CPU_load = []
for i in range(psutil.cpu_count()):
	CPU_load.append(((PERCPU_exit[i].user - PERCPU_start[i].user) / (PERCPU_exit[i].user -
    PERCPU_start[i].user + PERCPU_exit[i].idle - PERCPU_start[i].idle)) * 100 // 1)
print 'CPU_load: ', CPU_load
