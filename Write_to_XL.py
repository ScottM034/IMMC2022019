#Importing Libraries
import importlib
import xlsxwriter
#prompt for name of Exel File
name = input("Name of File:  ")
#creation of exel file
workbook = xlsxwriter.Workbook('{}.xlsx'.format(name))
worksheet = workbook.add_worksheet()
#defining variables
results = []
row = 1
col = 0
print("test run")
#setting up the exel documetn
worksheet.write(0,0,"Trial")
worksheet.write(0,1,"Turns Taken")
worksheet.write(0,2,"Walking Turns")
worksheet.write(0,3,"Delay in Turns")
worksheet.write(0,4,"Turns Saved")
worksheet.write(0,5,"Total time")
worksheet.write(0,6,"Walking Time")
worksheet.write(0,7,"Delay Time")
worksheet.write(0,8,"Time Saved")
#running the model script for a test
import WaterFall
#looping the script for multiple trials
for i in range(5000):
    #reloading the model
    importlib.reload(WaterFall)
    #colum number
    worksheet.write(row, col, i + 1)
    #grabbing variables from the script and writing them into excel cells
    worksheet.write(row, col + 1, WaterFall.total_time)
    worksheet.write(row, col + 2, WaterFall.walking_time)
    worksheet.write(row, col + 3, WaterFall.bag_time_or_shift/0.65)
    worksheet.write(row, col + 4, WaterFall.added_time)
    worksheet.write(row, col + 5, WaterFall.total_time*0.65)
    worksheet.write(row, col + 6, WaterFall.walking_time*0.65)
    worksheet.write(row, col + 7, WaterFall.bag_time_or_shift)
    worksheet.write(row, col + 8, WaterFall.added_time*0.65)
    i += 1
    row += 1
    print("turn",i)

#calculating averages using exel functions
worksheet.write(4,9,("Turns"))
worksheet.write(4,10,("Walking Turns"))
worksheet.write(4,11,("Delay in Turns"))
worksheet.write(4,12,("Turns Saved"))
worksheet.write(4,13,("Total Time"))
worksheet.write(4,14,("Walking Time"))
worksheet.write(4,15,("Delay Time"))
worksheet.write(4,16,("Time Saved"))
worksheet.write(5,9,"=AVERAGE(B2:B5001)")
worksheet.write(5,10,"=AVERAGE(C2:C5001)")
worksheet.write(5,11,"=AVERAGE(D2:D5001)")
worksheet.write(5,12,"=AVERAGE(E2:E5001)")
worksheet.write(5,13,"=AVERAGE(F2:F5001)")
worksheet.write(5,14,"=AVERAGE(G2:G5001)")
worksheet.write(5,15,"=AVERAGE(H2:H5001)")
worksheet.write(5,16,"=AVERAGE(I2:I5001)")
workbook.close()