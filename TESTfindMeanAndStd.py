import csv
import statistics
import pandas
import multiprocessing
import concurrent.futures
import time
import math


inputFileList = []

inputlength = int(input("Enter number of input files(Only Non-Control): "))

for i in range (0, inputlength):
    inputFileList.append([])
    nodem_file = input("Enter file name1 : ")
    inputFileList[i].append(nodem_file)
    dem_file = input("Enter file name2 : ")
    inputFileList[i].append(dem_file)

def findMeanandStd(dem_file):
    s = ()
    with open(dem_file) as csvfile:

        pandaDemFile = pandas.read_csv(dem_file)
        rows = pandaDemFile.shape[0]
        columns = pandaDemFile.shape[1]

        csv_reader = csv.reader(csvfile,delimiter = ',')
        line_count = 0
        sum_of_gene = 0

        with open(f"output-{dem_file}", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Mean","STD"])

            for row in csv_reader:
                if line_count < 1:
                    line_count += 1
                else:
                        for i in range (2,int(columns)):
                            sum_of_gene += float(row[i])
                            s = s + (float(row[i]),)
                        hello = statistics.stdev(s)
                        print("Standard Deviation of sample is % s " % (hello)) 
                        mean_of_gene = sum_of_gene/(columns -2)
                        print(f'\t{row[0]} And the mean is'+str(mean_of_gene))

                        writer.writerow([mean_of_gene, hello])
                        s = ()
                        sum_of_gene = 0
                        line_count += 1
            print(f'Processed{line_count} lines.')
    return(f"output-{dem_file}")


def findNumCol(pandaFile):
    numCol = pandaFile.shape[1]-2
    return numCol


def Compare(x1,x2,s1,s2,n1,n2):

    t = abs((x1 - x2) / (math.sqrt( ((s1 ** 2 )/ n1)  +  ((s2 ** 2 )/ n2)  )))
    dof = n1 + n2 -2
    return [t,dof]



def processFile(inputFile1, inputFile2):

    
    alz_file = pandas.read_csv(inputFile1)
    noDem_file = pandas.read_csv(inputFile2)
    mean_alz_file = pandas.read_csv(findMeanandStd(inputFile1))
    mean_noDem_file = pandas.read_csv(findMeanandStd(inputFile2))

    with open(f'Results-{inputFile1}_+_{inputFile2}', 'w', newline='') as file:

        writer = csv.writer(file)
        writer.writerow(["T-Score","DOF"])


        for i in range (mean_alz_file.shape[0]):


            d = Compare(mean_alz_file["Mean"][i] , 
                        mean_noDem_file["Mean"][i], 
                        mean_alz_file["STD"][i] , 
                        mean_noDem_file["STD"][i], 
                        findNumCol(alz_file), 
                        findNumCol(noDem_file) )
        
        
        
            writer.writerow(d)
if __name__ == '__main__':

    for i in range(len(inputFileList)):
        processFile(inputFileList[i][0],inputFileList[i][1])
