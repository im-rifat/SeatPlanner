from studentdata import Studentdata
from seatplanning import Seatplanning

daywise_excel_path = "modified_Excel_daywise_analysis.xlsx"
seatplan_excel_path = "modified_Seat-plan-3rd.xlsx"

sd = Studentdata(daywise_excel_path, Seatplanning(seatplan_excel_path))
sd.load()
