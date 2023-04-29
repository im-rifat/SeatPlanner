from openpyxl import load_workbook
from seatplanning import Seatplanning


class Studentdata:
    def __init__(self, path, sp: Seatplanning) -> None:
        self.path = path
        self._list = []
        self.sp = sp

    def load(self):
        wbDaywise = load_workbook(self.path)

        for ws in wbDaywise.worksheets:
            print(ws.title)
            regList = []

            for i, row in enumerate(ws):
                if i == 0:
                    continue
                regList.append(row[0].value)

            if len(regList) == 0:
                continue

            for i, roll in enumerate(regList):
                print(i, roll)

            self.sp.start_planning(regList, ws.title)
            break
