import os
import subprocess

res = subprocess.Popen('tasklist /FI "ImageName eq nginx.exe"', stdout=subprocess.PIPE)
lines = res.stdout.readlines()
lines = filter(lambda arg: arg.decode('utf-8', errors='ignore').startswith('nginx'), lines)
lines = list(lines)
# print(lines)
# for line in lines:
#    print(line)
count = len(lines) # 获取nginx进程个数

print(count)
