#!/bin/python3
# will execute command like
# 'cat filename'
# 'du -h filename'
# 'chmod +x filename'

import subprocess

proc1 = subprocess.run(["ls", "."], check=True)
proc_inst = subprocess.run(["cat", "explore_os.py"])
print(proc_inst)
proc_inst = subprocess.run(["cat", "explore_glob.py"], capture_output=True)
print(proc_inst)
