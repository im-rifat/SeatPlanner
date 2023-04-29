from openpyxl import load_workbook
from seatlookup import Seatlookup


class Seatplanning:
    def __init__(self, path) -> None:
        self.path = path
        self.mapping = {}
        self.index = 0

    def _get_index(self, index):
        self.index += 1
        print(self.index, self.mapping.get(index))
        if self.mapping.get(index):
            if self.mapping.get(self.index-1):
                return -1

            self.mapping[self.index-1] = True
            return self.index - 1
        else:
            self.mapping[index] = True
            return index

    def start_planning(self, rollList, savedfilename):
        q, mod = divmod(len(rollList), 3)
        print(q, mod)

        wb = load_workbook(self.path)

        index = [0, 0, 0]

        for sheet in wb.worksheets:
            sl = Seatlookup(sheet)
            seatList = sl.formatted_list()

            if len(seatList) == 0:
                continue

            for table in seatList:
                for row in table:
                    for i, col in enumerate(row):
                        ii = self._get_index(q*i + index[i])
                        print(i, col, ii)

                        try:
                            sheet[col] = rollList[ii]
                        except IndexError:
                            print("Index out of bounds exception")
                    index[0] += 1
                    index[1] += 1
                    index[2] += 1

#            print(sheet.title, seatList)

            # for row in sheet:
            #     for cell in row:
            #         print(cell.value)

            #         value = cell.value.split(":")

            #         result = re.search(r"([A-Z]+)(\d+)", value[0])

            #         col1 = result.group(1)
            #         row1 = int(result.group(2))
            #         left = int(value[1])
            #         bottom = int(value[2])

            #         for i in range(bottom):
            #             for j in range(left):
            #                 print(trie*j + index[j])
            #                 wbSeatSheet[chr(ord(col1)+j) + str((row1+i))
            #                             ] = regList[trie*j + index[j]]
            #             index[0] += 1
            #             index[1] += 1
            #             index[2] += 1

            #         print(value, result.groups())

            format = ".xlsx"
            wb.save(filename=f'{savedfilename}{format}')
        pass
