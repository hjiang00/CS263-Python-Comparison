import os
import psutil
import subprocess
import time
from memory_profiler import profile

#@profile
def test_in_python():
	sub_thread_time = subprocess.Popen("/usr/bin/time -lp pypy fibonacci3.py 100", shell = True, creationflags =0)
	#Mem info
	memory_useinfo = 0
	#Basic time
	start_time = time.time()
	#Thread1:
	sub_thread = subprocess.Popen('pypy fibonacci3.py 100', shell = True, creationflags = 0)
	#Log cpu_time, memory_useinfo
	while sub_thread.poll() is None:
		try:
			cpu_time = psutil.Process(sub_thread.pid).cpu_times()
			memory_useinfo = max(psutil.Process(sub_thread.pid).memory_info().rss, memory_useinfo)
		except:
			break
	#Info
	print 'System time: ', cpu_time.system
	print 'User time: ', cpu_time.user

	print 'CPU time: ', cpu_time.user + cpu_time.system
	print 'Real time: ', time.time() - start_time
	print 'Memory usage: ', memory_useinfo, 'Byte'
	#print 'Memory usage: ', str(round(memory_useinfo / 1024, 0)), 'KB'

	#Thread2:
	#sub_thread_time = subprocess.Popen("time TIMEFORMAT=$'Real_time %2R User_time %2U System_time %2S' python fibonacci3.py 100", shell = True, creationflags =0)
	#sub_thread_time = subprocess.Popen("/usr/bin/time -lp python fibonacci3.py 100", shell = True, creationflags =0)


if __name__ == '__main__':
	test_in_python()     
