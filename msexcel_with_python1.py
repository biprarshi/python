import xlsxwriter

workbook1 = xlsxwriter.Workbook("charts_msexcel1.xlsx")

worksheet1 = workbook1.add_worksheet()
worksheet1.name = "wrksheet1"
bold1 = workbook1.add_format({"bold": 1})
# tatar1 = workbook1.add_format({"underline":True,"italic":True,"align":"left"})

# create a data list
headings1 = ['Category', 'Values']
data1 = [
    ["Apple", "Cherry", "Pecan"],
    [60, 30, 10]
]


worksheet1.write_row("A1", headings1, bold1)
# worksheet1.write(0,2,"Namma",bold1)
worksheet1.write_column("A2", data1[0])
worksheet1.write_column("B2", data1[1])
# worksheet1.write_column(row=1,col=2,data=["Guddu","Rahul","Jeetu"],cell_format=tatar1)

chart1 = workbook1.add_chart({'type':'pie'})

# Add a data series to a chart using add_series method.
# Configure the first series. [sheetname, first_row, first_col, last_row, last_col]

chart1.add_series({
    # 'name':'Pie Sales Datam',
    'categories': ['wrksheet1', 1, 0, 3, 0],
    'values': ['wrksheet1', 1, 1, 3, 1]
})

chart1.set_title({'name':'Popular Pie Types'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(10)

# Insert the chart into the worksheet(with an offset).
# the top-left corner of a chart is anchored to cell C2.
worksheet1.insert_chart('C2',chart1,{'x_offset':25,'y_offset':10})

worksheet2 = workbook1.add_worksheet("wrksheet2")
headings1 = ['Category', 'Values']
data1 = [
    ['Q1', 'Q2', 'Q3', 'Q4'],
    [125, 60, 100, 80]
]
worksheet2.write_row('A1', headings1, bold1)
worksheet2.write_column('A2', data1[0])
worksheet2.write_column("B2", data1[1])

chart2 = workbook1.add_chart({'type':'pie'})
chart2.add_series({
    'name':'Quarterly Sales Data',
    'categories': ['wrksheet2',1,0,4,0],
    'values': ['wrksheet2',1,1,4,1],
    'data_labels':{'percentage':True}
})
chart2.set_title({'name':'Pie Chart of Quarterly Sales'})
worksheet2.insert_chart('D2',chart2)
worksheet3 = workbook1.add_worksheet('wrksheet3')
data1 = [
    [10, 20, 30, 40, 50],
    [20, 40, 60, 80, 100],
    [30, 60, 90, 120, 150]
]
worksheet3.write_column('A1', data1[0])
worksheet3.write_column(0, 1, data1[1])
worksheet3.write_column(0, 2, data1[2])

chart3 = workbook1.add_chart({'type':'column'})
chart3.add_series({'values': '=wrksheet3!$A$1:$A$5'})
chart3.add_series({'values': '=wrksheet3!$B$1:$B$5'})
chart3.add_series({'values': '=wrksheet3!$C$1:$C$5'})

worksheet3.insert_chart('B7',chart3)

worksheet4 = workbook1.add_worksheet('wrksheet4')
# Add the worksheet data that the charts will refer to
data1 = [
    ['Name', 'Physics', 'Maths'],
    ['Jay', 30, 60],
    ['Mohan', 40, 50],
    ['Veeru', 60, 70]
]
for i, details1 in enumerate(data1):
    worksheet4.write_row(i, 0, details1)

chart4 = workbook1.add_chart({'type':'column'})
chart4.add_series({
    'name':'=wrksheet4!$B$1',
    'categories':'=wrksheet4!$A$2:$A$4',
    'values':'=wrksheet4!$B$2:$B$4'
})

chart4.add_series({
    'name': ['wrksheet4', 0, 2],
    'categories': ['wrksheet4', 1, 0, 3, 0],
    'values': ['wrksheet4', 1, 2, 3, 2]
})

worksheet4.insert_chart('B7',chart4)


worksheet5 = workbook1.add_worksheet("wrksheet5")
headings1 = ["Number", "Batch1", "Batch2"]
data1 = [
    [2, 3, 4, 5, 6, 7],
    [70, 65, 55, 60, 50, 40],
    [60, 50, 60, 20, 10, 20]
]
worksheet5.write_row('A1', headings1, bold1)
worksheet5.write_column('A2', data1[0])
worksheet5.write_column('B2', data1[1])
worksheet5.write_column('C2', data1[2])

# '=Sheet1!$A$1' is equivalent to ['Sheet1', 0, 0].

chart5 = workbook1.add_chart({'type':'line'})
chart5.add_series({
    'name':['wrksheet5',0,1],
    'categories':['wrksheet5',1,0,6,0],
    'values':['wrksheet5',1,1,6,1]
})
chart5.add_series({
    'name': ['wrksheet5',0,2],
    'categories': ['wrksheet5', 1, 0, 6, 0],
    'values': ['wrksheet5', 1, 2, 6, 2]
})
chart5.set_title({'name':"Results of Data Analysis"})
chart5.set_x_axis({'name':'Test Number'})
chart5.set_y_axis({'name':'Data Length(mm)'})
chart5.set_style(11)
worksheet5.insert_chart('D2',chart5,{'x_offset':25,'y_offset':10})

workbook1.close()
