import xlrd
from Library.Config import Config
#From library package ,we import config file and import config class

class ReadExcel:

#this method is to read the 1st sheet of the excel sheet and locate the elements of the web page.

    def read_locators(self,sheetname):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(sheetname)
        rows = worksheet.get_rows()
        header=next(rows)
        print(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)
        return d

#this method is to read the 2nd excel sheet and send_keys via the excel sheet.

    def read_keys(self,sheetname):
        workbook2 = xlrd.open_workbook(Config.DATA_PATH)
        worksheet2 = workbook2.sheet_by_name(sheetname)
        col = worksheet2.ncols
        rows=worksheet2.get_rows()
        header=next(rows)
        d1 = []
        for row in rows:
            values=()
            for j in range(col):
                values+=(row[j].value,)
            d1.append(values)
        return d1






