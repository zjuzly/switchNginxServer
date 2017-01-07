import os
import subprocess

def startswith(sstr, ch):
    return sstr.lstrip().startswith(ch)


f = open('./nginx.conf', 'r')
lines = f.readlines()
length = len(lines)

index = 0
while index < length:
    if not lines[index].strip():
        index = index + 1
        continue
    print(lines[index])
    if ('server_name test.note.youdao.com' in lines[index]) or ('server_name note.youdao.com' in lines[index]):
        status = 'normal'
        if startswith(lines[index], '#'):
            status = 'comment'
        while True:
            if not lines[index].strip():
                index = index + 1
                continue
            # print(lines[index])
            if status == 'comment':
                strp = lines[index].lstrip()
                lines[index] = strp[1:].ljust(len(lines[index]))
            else:
                lines[index] = '#' + lines[index]
            if '}' in lines[index]:
                break
            index = index + 1
    index = index + 1

f.close()

f = open('./nginx.conf', 'w')
f.writelines(lines)

res = subprocess.Popen('tasklist /FI "ImageName eq nginx.exe"', stdout=subprocess.PIPE)
lines = res.stdout.readlines()
lines = filter(lambda arg: arg.decode('utf-8', errors='ignore').startswith('nginx'), lines)
lines = list(lines)
count = len(lines) # 获取nginx进程个数

print(count)
