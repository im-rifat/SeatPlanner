import re
from typing import List

REGEX_PATTERN = r"([A-Z]+)(\d+)"


class Seatlookup:
    def __init__(self, worksheet):
        self.listOfCoordinate = []
        for row in worksheet:
            for cell in row:
                if cell.value == '-':
                    self.listOfCoordinate.append(cell.coordinate)

    def print(self):
        print(self.formatted_list())

    def formatted_list(self) -> List[List[str]]:
        _tList = []
        _tSet = set()
        columns = []
        row = -1
        _list = []

        for item in self.listOfCoordinate:
            # print(item)
            result = re.search(REGEX_PATTERN, item)
            _tSet.add(result.group(1))
            if row != result.group(2):
                row = result.group(2)
                if len(_tList) != 0:
                    _list.append(_tList)

                _tList = []
                _tList.append(item)

            elif row == result.group(2):
                _tList.append(item)

        if len(_tList) != 0:
            _list.append(_tList)
        # print(_list)

        newList = []

        columns = list(_tSet)
        columns.sort()

        _tList = []
        table = Table()
        for index, item in enumerate(columns):
           # print(index, item)
            if len(_tList) != 0:
                table._addColumn(_tList)
            _tList = []

            for row in _list:
                for col in row:
                    if col.startswith(item):
                        _tList.append(col)

            if (index+1) % 3 == 0:
              #  print("table added")
                table._addColumn(_tList)
                _tList = []
              #  table.print_transpose_list()
                newList.append(table)
                table = Table()

        _list = []

        for item in newList:
            _list.append(item.transpose())

      #  print(_list)
        return _list


class Table:

    def __init__(self):
        self.list = []
        pass

    def _addColumn(self, tuple):
        self.list.append(tuple)

    def transpose(self):
        return list(map(list, zip(*self.list)))

    def print(self):
        for item in self.list:
            print(item)
            print("****************")

    def print_transpose_list(self):
        tlist = self.transpose()
        for item in tlist:
            print(item)
            print("****************")
