import csv

nodem_file = "testerfile.csv"

#fields = []
#rows = []

with open(nodem_file) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter = ',')
    line_count = 0
    sum_of_gene = 0
    
    for row in csv_reader:

        if line_count <= 1:
            print(f'Column names are {",".join(row)}')
            line_count += 1
        else:
            for i in range (2,53):
                sum_of_gene += float(row[i])
                print(f'\t{row[0]} has expressions {row[i]}.')
            mean_of_gene = sum_of_gene/50
            print('And the mean is'+str(mean_of_gene))
            sum_of_gene = 0
            line_count += 1
    
    print(f'Processed{line_count} lines.')
    
