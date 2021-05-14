import time
import os


def dis_time():
    cur_sec = time.localtime()
    cur_time = time.strftime("%H:%M:%S", cur_sec)
    cur_date = time.strftime("%d-%m", cur_sec)
    return cur_time, cur_date


def read_mac():
    macs = []
    data = open('macs.txt', encoding = 'utf8')
    for mac in data:
        mac = mac.strip('\n')
        macs.append(str(mac))
    data.close()
    print(macs)
    return macs


def write_down(name,line):
    now, date = dis_time()
    if date not in os.listdir():
        os.mkdir(f'{date}')
    data = open(f'{date}/{name}.txt', 'a')
    data.write(f'{now}  {line}\n')
    data.close()