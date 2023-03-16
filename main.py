import csv
import os

from openpyxl import Workbook

# create a new Excel workbook
workbook = Workbook()
sheet = workbook.active
file_path = os.path.join(os.getcwd(), '../test.txt')
# read the text file
with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter='|')
    # iterate over each row and add it to the Excel sheet
    for row in reader:
        # replace "_" with empty value
        row = ["" if col == "_" else col for col in row]
        sheet.append(row)

# save the Excel workbook
workbook.save('../test.xlsx')


if __name__ == "__main__":
    pass
