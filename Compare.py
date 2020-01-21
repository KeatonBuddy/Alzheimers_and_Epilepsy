import concurrent.futures
import time
import csv
import math

startTime = time.perf_counter()

difflist = []
def Compare(s1, s2, alist):
    difference = abs(float(s1)-float(s2))
    alist.append(difference)



with open('test.txt') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_number = 0

    for row in csv_reader:
        for i in range(2):
            Compare(row[i],row[i+1],difflist)

    print(difflist)

        


            













endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')
