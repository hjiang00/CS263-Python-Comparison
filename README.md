# CS263-Python-Comparison

## This is final project for CS263

## Progress:
  ## Week 3:

    1, configuration
    2, simple example try
    3, tool try
      timeit
      tracemalloc
      cProfile
      memory_profiler
      based on Cpython


  ## Week 4:
	1. VMware setting.
	2. BCC.
	3. Searching the useful algorithms that can be tested in all interpreters.
	4. Get all useful interpreters.
	5. Start testing time.
   
  ## Week 5:
	BCC Installation
	Credits to the repo of https://github.com/iovisor/bcc. With BCC tool, we are able to retrieve the performance data of python program in a more formal way. Since it requires Linux environment to install, in this week, we try to use AWS Linux environment to install the BCC tool.
	Correct Username commit
	We re-commit some files due to the username issues for zhicheng zhang since the username setting is not correct in             previous commits and it did not display contribution correctly.
	BCC test based on the Ubantu, and AWS.
	Time test based on the Linux, Mac.
	Time test based on single algorithm for Cpython and pypy.
	Memory test based on single algorithm for Cpython and pypy.
   
   ## Week 6:
	We found another way to test the memory usage of python program with the tool of memory profiler. This one can be easily installed on our machine without complicated environment setting. We planed to use this tool for memory usage analysis and compare it with BCC.
	We meet challenge in BCC, the speed is low and it cannot work for multiple interpreters, so we try another way to test performance.
	We start using Cpython to test all interpreters.

   ## Week 7:
	This week, we change our ideas and get huge progress. Firstly, as the other interpreter, as pypy, cannot use the same tool of Cpython, and it is unfair to use different tools. So, we want to use Cpython to test all the interpreters. So, we did the following things:
	1. Build a script of Cpython that use Cpython to test all other interpreters.
	2. Get the performance in Cpython based on the subprocess.
	3. Use psutil to test the Elapsed time, memory usage, CPU time, CPU_load.
	4. Use memory_profile to test memory.
	5. Use cProfile to get time.
	6. Start with Cpython, pypy, and then the Jython, IronPython and Cython.
   ## Week 8 && Final:
   	In week 8 and the rest weeks of this quarter, we decide to compare CPython, PyPy, Jython and Nuitka. We do not choose IronPython since it does not surpport very well on Mac OS. We test 11 algorithms among four different interpreters or compiler, and we test these algorithms with fixed inputs as well as multiple inputs. 
	In addition, we write a script file to parse all the testing output txt files and generate associated plots. Then we could analyze and conduct comparison with these data. 
	Finally, we complete presentation slides as well as final project report.
       
## Project setup:
	1.
