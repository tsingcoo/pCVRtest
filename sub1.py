import csv

with open('/Users/wangql/Downloads/pre/test.csv') as testf, open('/Users/wangql/Downloads/pre/submission.csv','w') as subf:
    fieldnames = ['instanceID', 'prob']
    writer = csv.DictWriter(subf, fieldnames=fieldnames)
    writer.writeheader()

    reader = csv.DictReader(testf)
    i = 0
    for row in reader:
        # print(row['instanceID'], 0.1)
        writer.writerow({'instanceID':row['instanceID'],'prob': '0.005'})
