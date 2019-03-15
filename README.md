# CS263-Python-Comparison

## This is final project for CS263
Our project is to conduct performance comparison for four different Python interpreters or compiler. They are CPython, Jython, PyPy, and Nuitka. We use 11 algorithms to perform testing and they are from https://pybenchmarks.org/ and https://benchmarksgame-team.pages.debian.net/benchmarksgame/. They are k-nucleotide, binary-trees, spectral-norm, thread-ring, reverse-complement, pi-digits, regex-DNA, pystone, n-body, Richards, fibonacci3.

## Measurement:
1. Psutil: Memory usage
2. Time(): Real time, User time
3. Terminal time: Real time, User time, Memory usage, Page reclaims, Context switches.
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
   ## Week 8 && Final week:
   	In week 8 and the rest weeks of this quarter, we decide to compare CPython, PyPy, Jython and Nuitka. We do not choose IronPython since it does not surpport very well on Mac OS. We test 11 algorithms among four different interpreters or compiler, and we test these algorithms with fixed inputs as well as multiple inputs. 
	In addition, we write a script file to parse all the testing output txt files and generate associated plots. Then we could analyze and conduct comparison with these data. 
	Finally, we complete presentation slides as well as final project report.
       
## Project setup:
All the testing algorithm files and the scripts, along with the outputs are in the folder Week 8. In the folder called output, it contains the graph as well as the text output files for each testing algorithm files. Below are the steps to run the test files and output the graphs.
1. In week 8 folder, there are 11 testing algorithm files such as pystone.py, richards.py... There are three testing files using text file as inputs and they are: l_k-nucleotide.py, l_reverse-complement.py, and regex-dna.py. The corresponding text input files are knucleotide-input2.txt, revcomp-input.txt and regexredux-input.txt. 
2. The script2.py is the file that help us to run specific testing file as well as output a txt file for the user time, real time, memory usage, etc.
3. Since we use terminal as well as other test tools including psutil to get the results, we have two output text files for each algorithm. In line 9, we need to define the file name for one of the output files. The format for terminal testing output file is: algorithmInitial-interpreterName-terminal.txt. For instance, binary tree with cpython is bi-cpython-terminal.txt. This step is essential since the parsing script will follow the name of output files to output the correct graphs. You can get the example in the folder of output. For another text output that using non-terminal tool for measurement, we need to mirror the output content when we run this script2.py, i.e. in terminal, we ran script2.py >> algorithmInitial-interpreterName.txt.
4. In line 10 and 17 of script2.py, we need to modify interpreter name and testing file name. Finally, in main function, we can call test_in_python() method with input.
5. To be notice that for Nuitka, which is an AOT compiler, we need to run .bin file instead of .py file by using “./xxx.bin” as input of test_in_python() method. These bin files are compiled on Mac OS so if you are using a different environment, you need to recompile first by executing nuitka xxx.py first.
6. After the text output files are generated correctly, we can use another script file to parse data and generate graph automatically. The file is called plotting.py in the folder of output. In the main function, we just need to call plot_data() and plot_data_terminal() for two different text output files. The input for these two functions is the algorithmInitial, for example, “bi” for binary tree algorithm. By running this script, we can generate all the graphs from the text output files accordingly.

After we gather all the testing data as well as the output graphs, we could analyze the performance and conduct comparison accordingly.
