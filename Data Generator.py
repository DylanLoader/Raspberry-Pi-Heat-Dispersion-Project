import os
file = open('n10000notreats5.txt', 'w')

def getCPUtemp():
    res=os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def calculate_primes():
    lower = 0
    upper = 10000
    trials = 0
    initial= (getCPUtemp())
    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               #print(num)
               continue
    final = getCPUtemp()
    difference = float(final) - float(initial)
    diff = str(difference)
    temp = (initial + ',' + final + ',' + diff + '\n')
    file.write(temp)
    trials += 1
    return trials
    

current_temp = float(getCPUtemp())
trials = calculate_primes()
while current_temp < 60 and trials < 200:
    calculate_primes()
    current_temp = float(getCPUtemp())
print('completed.')
file.close()

#print (float(getCPUtemp()))
# source code https://www.programiz.com/python-programming/examples/prime-number-intervals
# ,z  module https://github.com/kentwait/loadlog
# also used for temp module istats and psutil
