#!/usr/bin/env python3


import sys

import os
if not os.path.isfile('test.cfg')
    print('Config file does not exit')
    sys.exit()
if not os.path.isfile('user.csv') :
    print('User file does not exit')
    sys.exit()
if not os.path.isfile('gongzi.csv') :
    print('Gongzi file does not exit')
    sys.exit()



args= sys.argv[1:]
configfile = args[args.index('c') +1]
userdatafile = args[args.index('d') +1]
outputfile = args[args.index('o') +1]

Class Config(object):       
    def __init__(self, configfile):
        self._config = {}
        file1 = open(configfile)
	file2 = file1.readlines()
	for line in file2:
	    line.strip()
	    front_str = line.split('=')[0]
            back_str = line.split('=')[1]
	self._config[front_str] = int(back_str)
	file1.close()
    def get_config(self):
        return self._config(self)

canshu = Config(configfile)

Class Userdata(object):
    def __init__(self, userdatafile):
        self._userdata = []
	file3 = open(userdatafile)
	file4 = file3.readlines()
	for line in file4:
	    front_num = line.split(',')[0]
	    sqsalary = line.split(',')[1]
	    self._userdata.append(int(sqsalary))
	file3.close()

    def calculator(self):
	tax_rate = 0
	sskcs = 0
	if  sqsalary < canshu.get_config('JiShuL') and sqsalary >= 0:
	    jishu = canshu.get_config('JiShuL')
        elif  sqsalary >= canshu.get_config('JiShuL')  and sqsalary <= canshu.get_config('JiShuH')
            jishu = sqsalary
        elif  sqsalary > canshu.get_config('JiShuH')
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

    def dumptofile(self, outputfile)
        with open(outputfile, 'a') as file:
            outputfile.write(front_num + ',')
            outputfile.write(sqsalary + ',')
            outputfile.write(str(shebao) + ',')
            outputfile.write(str(geshui) + ',')
            outputfile.write(str(shsalary)) 

finalfile = Userdate(user.csv)
finalfile.calculator()
finalfile.dumptofile(gongzi.csv)
