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

alz_file = pandas.read_csv(r"C:\Users\sagor\Desktop\MDSC 397\project\ABA Alz\MDSC-397-master\finalsheet_demalz.csv")
noDem_file = pandas.read_csv(r"C:\Users\sagor\Desktop\MDSC 397\project\ABA Alz\MDSC-397-master\finalsheet_nodem.csv")
mean_alz_file = pandas.read_csv(r"C:\Users\sagor\Desktop\MDSC 397\project\ABA Alz\MDSC-397-master\mean_alz_file.csv")
mean_noDem_file = pandas.read_csv(r"C:\Users\sagor\Desktop\MDSC 397\project\ABA Alz\MDSC-397-master\mean_n0dem_file.csv")


print(mean_alz_file.shape[0])
with open('ComparedFile.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["T-Score","DOF"])
    for i in range (mean_alz_file.shape[0]):
        d = Compare(mean_alz_file["Mean"][i] , mean_noDem_file["Mean"][i], mean_alz_file["STD"][i] , mean_noDem_file["STD"][i], findNumCol(alz_file), findNumCol(noDem_file) )
        writer.writerow(d)

        





endTime = time.perf_counter()

print(f'Time taken: {endTime-startTime}')
