import concurrent.futures
import time
import csv
import math

startTime = time.perf_counter()

def Compare(s1, s2):
    difference = abs(float(s1)-float(s2))
    print(difference)



with open('test.txt') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_number = 0
    for row in csv_reader:
        Compare(row[1],row[2])
            













endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')