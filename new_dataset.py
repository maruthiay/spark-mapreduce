#!/usr/bin/env python

import subprocess
list2 = [1000000,10000000,100000000,200000000]
list1 = [2,3,4,5,6]
for i in list1:
        for j in list2:
                print(i,j)
                result = subprocess.check_output(['./generate',str(j),str(i)])
                f = open('output'+str(i)+str(j)+'.txt', 'w')
                f.write(result)
                f.close()
