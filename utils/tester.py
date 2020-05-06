import csv

with open('fma_metadata/tracks.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 2
    for row in csv_reader:
        if line_count == 2:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if str(row[40]) != "":
                thing = row[0].zfill(6)
                print(f'\t{thing} {row[40]}')
            
            line_count += 1
    #print(f'Processed {line_count} lines.')
