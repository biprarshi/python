import xlsxwriter

wrkbook1 = xlsxwriter.Workbook("test1.xlsx")
wrksheet1 = wrkbook1.add_worksheet(name="newsheet1")
tatar1 = wrkbook1.add_format(
    {'underline': True, 'italic': True, 'align': 'left'})
bold1 = wrkbook1.add_format({'bold': True})
headings1 = ["Category", "Price", "User"]
data1 = [
    ["apple", "cinnamon", "mint"],
    [10, 20, 40]
]
wrksheet1.write_row('A1', data=headings1, cell_format=bold1)
wrksheet1.write(5, 5, "fish", bold1)
wrksheet1.write_column(1, 0, data1[0], tatar1)
wrksheet1.write_column(1, 1, data1[1])
wrksheet1.write_column(1, 2, ["ghum", "morpheus", "neo"], tatar1)
chart1 = wrkbook1.add_chart({'type': 'pie'})

chart1.add_series({
    'name': 'spices',
    'categories': ['newsheet1', 1, 0, 3, 0],
    'values': ['newsheet1', 1, 1, 3, 1]
})
chart1.set_title({"name": "spices"})
chart1.set_style(10)
chart1.set_size({'height': 500, 'width': 500})
wrksheet1.insert_chart(6, 6, chart1, {'x_offset': 10, 'y_offset': 10})
# --------------------------------------------------
wrksheet2 = wrkbook1.add_worksheet(name="newsheet2")
headings2 = ["sname", "marks"]
data2 = [
    ["guddu", "toy", "lolo", "singh"],
    [67, 77, 34, 99]
]
wrksheet2.write_row(0, 0, headings2)
wrksheet2.write_column(1, 0, data2[0])
wrksheet2.write_column(1, 1, data2[1])
chart2 = wrkbook1.add_chart({'type': "pie"})
chart2.set_title({'name': 'Marks'})
chart2.set_style(10)
chart2.set_size({"height": 400, "width": 250})
chart2.add_series({
    'name': 'marks',
    'categories': ['newsheet2', 1, 0, 4, 0],
    'values': ['newsheet2', 1, 1, 4, 1],
    'line': {'color': 'red', 'width': 8},
    'fill':   {'none': False}
})
wrksheet2.insert_chart(5, 5, chart2, {'x_offset': 10, 'y_offset': 15})
# -----------------------------------------------------------------------------------
wrksheet3 = wrkbook1.add_worksheet(name='newsheet3')
data3 = [
    ['ram', 'guddu', 'sam', 'rohit', 'tara'],
    [10, 20, 30, 40, 50],
    [5, 15, 25, 35, 45],
    [23, 19, 36, 44, 9]
]
wrksheet3.write_row(0, 0, ("name", "dataset1", "dataset2",
                    "dataset3"), cell_format=bold1)
wrksheet3.write_column(1, 0, data3[0])
wrksheet3.write_column(1, 1, data3[1])
wrksheet3.write_column(1, 2, data3[2])
wrksheet3.write_column(1, 3, data3[3])
chart3 = wrkbook1.add_chart({'type': 'column'})
chart3.set_size({'height': 400, 'width': 400})
chart3.set_style(10)
chart3.set_title({"name": "Datasets"})
chart3.add_series({
    'name': 'Datasets1',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 1, 1, 5, 1]

})
chart3.add_series({
    'name': 'Datasets2',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 1, 2, 5, 2]})
chart3.add_series({
    'name': 'Datasets3',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 1, 3, 5, 3]
})
wrksheet3.insert_chart(5, 5, chart3, {'x_offset': 10, 'y_offset': 12})
# -------------------------------------------------------------------------------------
wrksheet4 = wrkbook1.add_worksheet(name='newsheet4')
chart4 = wrkbook1.add_chart({'type': 'column'})
chart4.set_size({'height': 400, 'width': 400})
chart4.set_style(10)
chart4.set_title({"name": "Datasets"})
chart4.add_series({
    'name': f'{data3[0][0]}',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 1, 1, 1, 3]

})
chart4.add_series({
    'name': f'{data3[0][1]}',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 2, 1, 2, 3]

})
chart4.add_series({
    'name': f'{data3[0][2]}',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 3, 1, 3, 3]

})
chart4.add_series({
    'name': f'{data3[0][3]}',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 4, 1, 4, 3]

})
chart4.add_series({
    'name': f'{data3[0][4]}',
    'categories': ['newsheet3', 0, 1, 0, 3],
    'values': ['newsheet3', 5, 1, 5, 3]

})


wrksheet4.insert_chart(5, 5, chart4, {'x_offset': 0, 'y_offset': 0})


wrkbook1.close()
