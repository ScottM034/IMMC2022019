#Importing Libraries
import importlib
import xlsxwriter
#prompt for name of Exel File
name = input("Name of File:  ")
#creation of exel file
workbook = xlsxwriter.Workbook('{}.xlsx'.format(name))
worksheet = workbook.add_worksheet()
#defining variables
Total_Time1 = 0
Total_Time2 = 0
Walking_Time1 = 0
Bag_and_shift_time1 = 0
Time_Saved1 = 0
Walking_Time2 = 0
Bag_or_shift_time_2 = 0
Time_saved2 = 0
Walking_Time_Final = 0
Bag_or_Shift_Time_Final = 0
Time_Saved_Final = 0
Final_Time_Final = 0
row = 0
col = 0
print("test run")
#running the model script for a test
import SeatOrderPlaneType3
#looping the script for multiple trials
for i in range(1000):
    #reloading the model
    importlib.reload(SeatOrderPlaneType3)
    #taking 2 seperat trials
    Total_Time1 = SeatOrderPlaneType3.total_time
    Walking_Time1 = SeatOrderPlaneType3.walking_time
    Bag_and_shift_time1 = SeatOrderPlaneType3.bag_time_or_shift/0.65
    Time_Saved1 = SeatOrderPlaneType3.added_time
    #Taking 2 seperate Trials
    importlib.reload(SeatOrderPlaneType3)
    Total_Time2 = SeatOrderPlaneType3.total_time
    Walking_Time2 = SeatOrderPlaneType3.walking_time
    Bag_or_shift_time_2 = SeatOrderPlaneType3.bag_time_or_shift/0.65
    Time_saved2 = SeatOrderPlaneType3.added_time
    #Taking the higher one of the 2
    if Total_Time1 >= Total_Time2:
        Final_Time_Final = Total_Time1
        Walking_Time_Final = Walking_Time1
        Bag_or_Shift_Time_Final = Bag_and_shift_time1
        Time_Saved_Final = Time_Saved1
    else:
        Final_Time_Final = Total_Time2
        Walking_Time_Final = Walking_Time2
        Bag_or_Shift_Time_Final = Bag_or_shift_time_2
        Time_Saved_Final = Time_saved2
    #setting up the excel
    worksheet.write(row, col + 1, Final_Time_Final)
    worksheet.write(row, col + 2, Walking_Time_Final)
    worksheet.write(row, col + 3, Bag_or_Shift_Time_Final)
    worksheet.write(row, col + 4, Time_Saved_Final)
    worksheet.write(row, col + 5, Final_Time_Final*0.65)
    worksheet.write(row, col + 6, Walking_Time_Final*0.65)
    worksheet.write(row, col + 7, Bag_or_Shift_Time_Final*0.65)
    worksheet.write(row, col + 8, Time_Saved_Final*0.65)
    i += 1
    row += 1
    print("turn",i)
#setting up the exel documetn
worksheet.write(4,9,("Turns"))
worksheet.write(4,10,("Walking Turns"))
worksheet.write(4,11,("Delay in Turns"))
worksheet.write(4,12,("Turns Saved"))
worksheet.write(4,13,("Total Time"))
worksheet.write(4,14,("Walking Time"))
worksheet.write(4,15,("Delay Time"))
worksheet.write(4,16,("Time Saved"))
worksheet.write(5,9,"=AVERAGE(B2:B1001)")
worksheet.write(5,10,"=AVERAGE(C2:C1001)")
worksheet.write(5,11,"=AVERAGE(D2:D1001)")
worksheet.write(5,12,"=AVERAGE(E2:E1001)")
worksheet.write(5,13,"=AVERAGE(F2:F1001)")
worksheet.write(5,14,"=AVERAGE(G2:G1001)")
worksheet.write(5,15,"=AVERAGE(H2:H1001)")
worksheet.write(5,16,"=AVERAGE(I2:I1001)")
workbook.close()