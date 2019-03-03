import matplotlib.pyplot as plt
import re
#import pandas as pd
import numpy as np

# same algorithm with different input/interpreter
def collect_data(interpreter, method):
    sysTime = []
    userTime = []
    cpuTime = []
    realTime = []
    memUse = []
    fileName = None
    if interpreter == "cpython":
        fileName = method + "-cpython.txt"
    elif interpreter == "jython":
        fileName = method + "-jython.txt"
    elif interpreter == "pypy":
        fileName = method + "-pypy.txt"
    elif interpreter == "nuitka":
        fileName = method + "-nuitka.txt"

    with open(fileName, "r") as f:
        file = f.readlines()

        for line in file:
            data = re.split("[: ]+", line)
            if data[0].startswith('S'):
                sysTime.append(data[2])
            elif data[0].startswith('U'):
                userTime.append(data[2])
            elif data[0].startswith('C'):
                cpuTime.append(data[2])
            elif data[0].startswith('R'):
                realTime.append(data[2])
            elif data[0].startswith('M'):
                memUse.append(data[2])
            else:
                continue

    return sysTime, userTime, cpuTime, realTime, memUse

def collect_terminal_data(interpreter, method):
    sysTime = []
    userTime = []
    realTime = []
    memUse = []
    pageReclaim = []
    volSwitch = []
    involSwitch = []
    fileName = None
    if interpreter == "cpython":
        fileName = method + "-cpython-terminal.txt"
    elif interpreter == "jython":
        fileName = method + "-jython-terminal.txt"
    elif interpreter == "pypy":
        fileName = method + "-pypy-terminal.txt"
    elif interpreter == "nuitka":
        fileName = method + "-nuitka-terminal.txt"
    with open(fileName, "r") as f:
        file = f.readlines()
        for line in file:
            data = re.split("[ ]+", line)
            category = None
            if len(data[0]) != 0:
                category = data[0]
            else:
                if data[2] == 'page':
                    category = data[3]
                else:
                    category = data[2]
            if 'real' in category:
                realTime.append(data[1])
            elif 'user' in category:
                userTime.append(data[1])
            elif 'sys' in category:
                sysTime.append(data[1])
            elif 'maximum' in category:
                memUse.append(data[1])
            elif 'reclaims' in category:
                pageReclaim.append(data[1])
            elif category == 'voluntary':
                volSwitch.append(data[1])
            elif 'involuntary' in category:
                involSwitch.append(data[1])
            else:
                continue
    print sysTime, userTime, realTime, memUse, pageReclaim, volSwitch, involSwitch
    return sysTime, userTime, realTime, memUse, pageReclaim, volSwitch, involSwitch

def plot_data(method):
    sys = {}
    user = {}
    cpu = {}
    real = {}
    mem = {}
    # Input and interpreter setting
    input = [10, 50, 100]
    interpreter = ["cpython", "jython"]
    for key in interpreter:
        tempsys, tempuser, tempcpu, tempreal, tempmem = collect_data(key, method)
        sys[key] = tempsys
        user[key] = tempuser
        cpu[key] = tempcpu
        real[key] = tempreal
        mem[key] = tempmem

    #Plot
    x = np.array(input)
    y1 = np.array(sys.get("cpython"))
    y2 = np.array(sys.get("jython"))
    plt.plot(x, y1, marker = 'o', markerfacecolor = 'blue', label = "cpython")
    plt.plot(x, y2, marker = 'o', markerfacecolor = 'red', label = "jython")
    plt.legend()
    plt.savefig('fib')

def plot_data_terminal(method):
    sys = {}
    user = {}
    real = {}
    mem = {}
    page = {}
    contexSwitch = {}
    # Input and interpreter setting
    input = [10, 50, 100]
    interpreter = ["cpython", "jython"]
    for key in interpreter:
        sysTime, userTime, realTime, memUse, pageReclaim, volSwitch, involSwitch = collect_terminal_data(key, method)
        #add vol and invol together
        contSwit = np.add(map(int, volSwitch), map(int, involSwitch))
        sys[key] = sysTime
        user[key] = userTime
        real[key] = realTime
        mem[key] = memUse
        page[key] = pageReclaim
        contexSwitch[key] = contSwit
    
    #Plot
    x = np.array(input)
    y1 = np.array(sys.get("cpython"))
    y2 = np.array(sys.get("jython"))
    plt.plot(x, y1, marker = 'o', markerfacecolor = 'blue', label = "cpython")
    plt.plot(x, y2, marker = 'o', markerfacecolor = 'red', label = "jython")
    plt.legend()
    plt.savefig('fib-terminal')


if __name__ == '__main__':
#    plot_data("fib")
#    collect_terminal_data("cpython", "fib")
    plot_data_terminal("fib")
