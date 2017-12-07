import re
from pprint import pprint
import matplotlib.pyplot as plt
import math

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_array(d, workload):
    y = []
    for i in workload:
        y.append(float(d[i])/math.pow(10, -6))
    return y

workload=[4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144]
workload_label=['4', '16', '64', '256', '1k', '4k', '16k', '64k', '256k']
numeric_const_pattern = r"(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?"
rx = re.compile(numeric_const_pattern, re.VERBOSE)
result_map = {}
for core in range(0, 4):
    workload_map = {}
    for w in workload:
        with (open(str(w) + '_' + str(core) + '.log')) as f:
            data = f.read()
        d = [s for s in data.split() if isFloat(s)]
        workload_map[w] = d[-2]
    result_map[core] = workload_map

handle = []
handle_label = ['0 to 0', '1 to 0', '2 to 0', '3 to 0']
for i in range(0, 4):
    y = get_array(result_map[i], workload)
    p, = plt.plot(workload, y)
    plt.xscale('log')
    plt.xticks(workload, workload_label)
    handle.append(p)
plt.xlabel('size (bytes)')
plt.ylabel('time (us)')
plt.legend(handle, handle_label, bbox_to_anchor=(0.05, 0.95), loc=2, borderaxespad=0.)
plt.savefig('binder-ipc.pdf')
