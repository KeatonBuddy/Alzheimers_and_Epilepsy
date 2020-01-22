import concurrent.futures
import time
import csv
import math

startTime = time.perf_counter()

diffdict = {}
def Compare(s1, s2, alist):
    difference = abs(float(s1)-float(s2))
    alist.append(difference)



with open('data1.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    header = csv_reader.fieldnames


    for row in csv_reader:

        for i in range(3):
            print(header[i])
            print(row[f'{header[i]}'])

            diffdict.setdefault(header[i],[])
            if header[i] == 'epilepsy genes':
                diffdict[header[i]].append(row[f'{header[i]}'])
            else:
                diffdict[header[i]].append(float(row[f'{header[i]}']))

    print(diffdict)
      

endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')