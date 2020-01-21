import concurrent.futures
import time
import csv
import math

startTime = time.perf_counter()

diffdict = {}
def Compare(s1, s2, alist):
    difference = abs(float(s1)-float(s2))
    alist.append(difference)



with open('test.txt') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    line_number = 0
    header = csv_reader.fieldnames
    for row in csv_reader:
        for i in range(3):
            print(header[i])
            print(row[f'{header[i]}'])
            diffdict.setdefault(header[i],[])
            diffdict[header[i]].append(row[f'{header[i]}'])
    print(diffdict)

        
        
        
        
        #for i in range(3):
         #   print(row.)


        


            













endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')
