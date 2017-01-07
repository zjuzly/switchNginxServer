import os
import subprocess
import re
import sys

def startswith(sstr, ch):
    return sstr.lstrip().startswith(ch)

filename = sys.argv[1] or './nginx.conf'
print(filename)
f = open(filename, 'r')
lines = f.readlines()
length = len(lines)

pattern = r'^(\s)*#?(\s)*server_name (test.)?note.youdao.com'
reg = re.compile(pattern)

index = 0
while index < length:
    if not lines[index].strip():
        index = index + 1
        continue
    if reg.match(lines[index]):
        status = 'normal'
        if startswith(lines[index], '#'):
            status = 'comment'
        while True:
            if not lines[index].strip():
                index = index + 1
                continue
            if status == 'comment':
                strp = lines[index].lstrip()
                lines[index] = strp[1:].ljust(len(lines[index]) - 1)
            else:
                lines[index] = '#' + lines[index]
            if '}' in lines[index]:
                break
            index = index + 1
    index = index + 1

f.close()

f = open(filename, 'w')
f.writelines(lines)
f.close()

res = subprocess.Popen('tasklist /FI "ImageName eq nginx.exe"', stdout=subprocess.PIPE)
lines = res.stdout.readlines()
lines = filter(lambda arg: arg.decode('utf-8', errors='ignore').startswith('nginx'), lines)
lines = list(lines)
count = len(lines) # 获取nginx进程个数
print(count)

if count < 2:
    print('start nginx....')
    os.system('start nginx')
else:
    print('reload nginx...')
    os.system('nginx -s reload')
