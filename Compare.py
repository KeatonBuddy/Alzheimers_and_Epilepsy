import concurrent.futures
import time
import csv
import math

startTime = time.perf_counter()

def Compare(s1, s2):
    difference = abs(s1-s2)
    print(difference)



with open('test.txt') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        id1 = row["ID"]
        print(id1)
              













endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')