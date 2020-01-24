import csv
import statistics
import pandas

nodem_file = input("Enter file name: ")
output_file = input("Enter file output name:")
s = ()

with open(nodem_file) as csvfile:

    pandaDemFile = pandas.read_csv(nodem_file)
    rows = pandaDemFile.shape[0]
    columns = pandaDemFile.shape[1]

    csv_reader = csv.reader(csvfile,delimiter = ',')
    line_count = 0
    sum_of_gene = 0

    with open(f"{output_file}", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Mean","STD"])

        for row in csv_reader:
            if line_count <= 1:
                line_count += 1
            else:
                    for i in range (2,int(columns)):
                        sum_of_gene += float(row[i])
                        s = s + (float(row[i]),)
                    hello = statistics.stdev(s)
                    print("Standard Deviation of sample is % s " % (hello)) 
                    mean_of_gene = sum_of_gene/(columns-2)
                    print(f'\t{row[0]} And the mean is'+str(mean_of_gene))

                    writer.writerow([mean_of_gene, hello])
                    s = ()
                    sum_of_gene = 0
                    line_count += 1
        print(f'Processed{line_count} lines.')
