import csv # pip install XlsxWriter
import os
from datetime import datetime


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)



createFolder('./db/')
# Creates a folder in the current directory called data

# Create an new Excel file and add a worksheet.

# workbook = xlsxwriter.Workbook('./db/Attch.csv')
# worksheet = workbook.add_worksheet()


# now=datetime.now() # recode current data
# File_Times=now.strftime("%d_%m_%Y") # Formath date "2021/03/12 Saturday 00:00:00"


# def markAttence(name):
#     with open ('./db/NU_Attch'+'_'+File_Times+'.csv','w',newline='') as f:
#         myDataList =f.readlines()
#         #print(myDataList)
#         nameList=[]
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             dtString=now.strftime("%Y/%m/%d %A %H:%M:%S") # Formath date "2021/03/12 Saturday 00:00:00"
#             f.writelines(f'\n{name},{dtString}')


# Widen the first column to make the text clearer.
# worksheet.set_column('A:A', 20)

# # Add a bold format to use to highlight cells.
# bold = workbook.add_format({'bold': True})

# # Write some simple text.
# worksheet.write('A1', 'Hello')

# # Text with formatting.
# worksheet.write('A2', 'World', bold)

# # Write some numbers, with row/column notation.
# worksheet.write(2, 0, 123)
# worksheet.write(3, 0, 123.456)

# # Insert an image.
# worksheet.insert_image('B5', 'logo.png')

# workbook.close()