import concurrent.futures
import time
import csv
import math
import pandas

startTime = time.perf_counter()


def findNumCol(pandaFile):
    numCol = pandaFile.shape[1]-2
    return numCol


def Compare(x1,x2,s1,s2,n1,n2):

    t = abs((x1 - x2) / (math.sqrt( ((s1 ** 2 )/ n1)  +  ((s2 ** 2 )/ n2)  )))
    dof = n1 + n2 -2
    return [t,dof]

alzFile = input("Enter file 1:")
noDem = input("Enter file 2:")
meanAlzFile = input("Enter mean file 1:")
meanNoDemFile = input ("Enter mean file 2:")



alz_file = pandas.read_csv(alzFile)
noDem_file = pandas.read_csv(noDem)
mean_alz_file = pandas.read_csv(meanAlzFile)
mean_noDem_file = pandas.read_csv(meanNoDemFile)



with open('ComparedFile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["T-Score","DOF"])
    for i in range (mean_alz_file.shape[0]):
        d = Compare(mean_alz_file["Mean"][i] , mean_noDem_file["Mean"][i], mean_alz_file["STD"][i] , mean_noDem_file["STD"][i], findNumCol(alz_file), findNumCol(noDem_file) )
        writer.writerow(d)

        





endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')
