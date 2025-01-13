import csv
import pandas

# with open("CsvFile.csv") as data_file:
#     # data = data_file.readlines()
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)



# After Installing Pandas , don't need to do all this stuff
data1 = pandas.read_csv("CsvFile.csv")
data_dict = data1.to_dict()
print(data_dict)

    