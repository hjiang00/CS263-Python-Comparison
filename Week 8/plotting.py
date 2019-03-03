import matplotlib.pyplot as plt
import re

# same algorithm with different interpreter
def collect_data(fileName):
    sysTime = []
    userTime = []
    cpuTime = []
    realTime = []
    memUse = []
    interpreter = [1, 2]
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

def plot_data():
    sys = {}
    user = {}
    cpu = {}
    real = {}
    mem = {}
    keys = ['cython', 'jtyhon']
    tempsys, tempuser, tempcpu, tempreal, tempmem = collect_data("output-fib-cython.txt")
    collect_data("output-fib-jython.txt")

if __name__ == '__main__':

