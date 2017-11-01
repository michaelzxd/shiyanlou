#!/usr/bin/env python3


import sys

import os
from multiprocessing import Process, Queue
queue1 = Queue()
queue2 = Queue()

args= sys.argv[1:]
configfile = args[args.index('-c') +1]
userdatafile = args[args.index('-d') +1]
outputfile = args[args.index('-o') +1]

class Config(object):
    def __init__(self,configfile):
        self._config = {}
        file1 = open(configfile)
        file2 = file1.readlines()
        for line in file2:
            front_str0 = line.split('=')[0]
            front_str = front_str0.strip()
            back_str0 = line.split('=')[1]
            back_str = back_str0.strip().strip('\n')
            self._config[front_str] = float(back_str)
        file1.close()
    def get_config(self,shebaocanshu):
        return self._config[shebaocanshu]
canshu = Config(configfile)

def duqu(userdatafile):
    file3 = open(userdatafile)
    for line in file3.readlines():
        shuju = []
        gonghao = int(line.split(',')[0])
        sqsalary = int(line.split(',')[1].strip('\n'))
        shuju.append(gonghao)
        shuju.append(sqsalary)
        queue1.put(shuju)
        print("read data",shuju)
    file3.close()

def jisuan():
    for i in range(0,queue1.qsize()):
        shuju1 = []
        sj =  queue1.get(i)
        gonghao = sj[0]
        sqsalary = sj[1] 
        tax_rate = 0
        sskcs = 0
        if  sqsalary < canshu.get_config('JiShuL') and sqsalary >= 0:
            jishu = canshu.get_config('JiShuL')
        elif  sqsalary >= canshu.get_config('JiShuL')  and sqsalary <= canshu.get_config('JiShuH'):
            jishu = sqsalary
        elif  sqsalary > canshu.get_config('JiShuH'):
            jishu = canshu.get_config('JiShuH')
        else:
            print('ParameterError')
        insurance = jishu * (canshu.get_config('YangLao') + canshu.get_config('YiLiao')  + canshu.get_config('ShiYe')  +  canshu.get_config('GongShang') + canshu.get_config('ShengYu') + canshu.get_config('GongJiJin'))
        ynssde = sqsalary - insurance - 3500

        if ynssde < 1500 and ynssde > 0:
            tax_rate = 0.03
            sskcs = 0
        elif ynssde >= 1500 and ynssde < 4500:
            tax_rate = 0.1 
            sskcs = 105
        elif ynssde >= 4500 and ynssde < 9000:
            tax_rate = 0.2
            sskcs = 555
        elif ynssde >= 9000 and ynssde < 35000:
            tax_rate = 0.25
            sskcs = 1005
        elif ynssde >= 35000 and ynssde < 55000:
            tax_rate = 0.3
            sskcs = 2755
        elif ynssde >= 55000 and ynssde < 80000:
            tax_rate = 0.35
            sskcs = 5505
        elif ynssde >= 80000:
            tax_rate = 0.45
            sskcs = 13505
        else:
            tax_rate = 0
            sskcs = 0

        tax = ynssde * tax_rate - sskcs
        shsalary = format(sqsalary - insurance - tax,'0.2f')
        geshui = format(tax, '0.2f')
        shebao = format(insurance,'0.2f')
        shuju1.append(str(gonghao))
        shuju1.append(str(sqsalary))
        shuju1.append(str(shebao))
        shuju1.append(str(geshui))
        shuju1.append(str(shsalary)+ '\n')
        print("cal data",shuju1)
        queue2.put(shuju1)

def xieru(outputfile):
    with open(outputfile,'a') as dst_file:
        for i in range(0,queue2.qsize()):
            shuju2 = queue2.get(i)
            print("write data",shuju2)
            for item in shuju2:
                print("item:",item)
                if item.endswith('\n'):
                    dst_file.write(item)
                else:
                    dst_file.write(str(item) + ',')

def main():
    dq = Process(target=duqu,args=(userdatafile,))
    dq.start()
    dq.join()
    js = Process(target=jisuan)
    js.start()
    js.join()
    xr = Process(target=xieru,args=(outputfile,))
    xr.start()
    xr.join()
if __name__ == '__main__':
    main()

