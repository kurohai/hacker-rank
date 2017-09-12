import subprocess
import sys

for i in xrange(100000, 999999):
    p = subprocess.Popen(['python', '01-once-in-a-tram.py', str(i)], shell=False, stderr=subprocess.STDOUT, stdout=sys.stdout)
    p.wait()
