import os
import psutil
import subprocess
import time
from memory_profiler import profile

#@profile
def test_in_python(input):
	log = open('pi-pypy-test.txt', 'a')
	sub_thread_time = subprocess.Popen("/usr/bin/time -lp pypy pidigits-jython.py " + input, shell = True, creationflags =0, stdout = log, stderr = log)
	#sub_thread_time = subprocess.Popen("/usr/bin/time -lp " + input, shell = True, creationflags =0, stdout = log, stderr = log)
	#Mem info
	memory_useinfo = 0
	#Basic time
	start_time = time.time()
	#Thread1:
	sub_thread = subprocess.Popen("pypy pidigits-jython.py " + input, shell = True, creationflags = 0)
	#sub_thread = subprocess.Popen('' + input, shell = True, creationflags = 0)
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
	print "\n"

	#Thread2:
	#sub_thread_time = subprocess.Popen("time TIMEFORMAT=$'Real_time %2R User_time %2U System_time %2S' python fibonacci3.py 100", shell = True, creationflags =0)
	#sub_thread_time = subprocess.Popen("/usr/bin/time -lp python fibonacci3.py 100", shell = True, creationflags =0)


if __name__ == '__main__':
	# test_in_python("./l_regex-dna.bin 7 0 < regexredux-input.txt")
	# test_in_python("./l_regex-dna.bin 8 0 < regexredux-input.txt")
	# test_in_python("./l_regex-dna.bin 9 0 < regexredux-input.txt")
	# test_in_python("./l_regex-dna.bin 10 0 < regexredux-input.txt")
	# test_in_python("./l_regex-dna.bin 11 0 < regexredux-input.txt")
	# test_in_python("./l_regex-dna.bin 12 0 < regexredux-input.txt")
	test_in_python("10000")
	test_in_python("15000")
	test_in_python("20000")
	test_in_python("25000")
	test_in_python("30000")
	test_in_python("35000")


	#test_in_python("./thread-ring.bin 1000000")
	# test_in_python("./fibonacci3.bin 10")
	# test_in_python("./fibonacci3.bin 50")
	# test_in_python("./fibonacci3.bin 100")
	# test_in_python("./fibonacci3.bin 200")
	# test_in_python("./fibonacci3.bin 500")
	# test_in_python("./fibonacci3.bin 1000")
	# test_in_python("./fibonacci3.bin 5000")
	# test_in_python("./fibonacci3.bin 10000")
