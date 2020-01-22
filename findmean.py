import csv

nodem_file = input("Enter file name: ")


with open(nodem_file) as csvfile:


    csv_reader = csv.reader(csvfile,delimiter = ',')
    line_count = 0
    sum_of_gene = 0

    if nodem_file == "finalsheet_nodem.csv":

        with open('mean_n0dem_file.csv', 'w', newline='') as file:

               for row in csv_reader:
                    if line_count <= 1:
                        #print(f'Column names are {",".join(row)}')
                        line_count += 1
                    else:
                         for i in range (2,53):
                              sum_of_gene += float(row[i])
                         #print(f'\t{row[0]} has expressions {row[i]}.')
                         mean_of_gene = sum_of_gene/50
                         print(f'\t{row[0]} And the mean is'+str(mean_of_gene))
                         writer = csv.writer(file)
                         writer.writerow([mean_of_gene])
                         sum_of_gene = 0
                         line_count += 1
               print(f'Processed{line_count} lines.')

    elif nodem_file == "finalsheet_demalz.csv":

        with open('mean_alz_file.csv','w', newline='') as file:

            for row in csv_reader:
                if line_count <= 1:
                    #print(f'Column names are {",".join(row)}')
                    line_count += 1
                else:
                    for i in range (2,37):
                        sum_of_gene += float(row[i])
                    #print(f'\t{row[0]} has expressions {row[i]}.')
                    mean_of_gene = sum_of_gene/35
                    print(f'\t{row[0]} And the mean is'+str(mean_of_gene))
                    writer = csv.writer(file)
                    writer.writerow([mean_of_gene])
                    sum_of_gene = 0
                    line_count += 1
    
