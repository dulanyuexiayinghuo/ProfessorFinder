import openpyxl


def write_excel(uni_departments):
    wb = openpyxl.Workbook()
    university = uni_departments[0]
    for department in uni_departments[1:]:
        print('processing:' + department.name)
        ws = wb.create_sheet(department.name, 0)
        ws.append(['学校', '院系', '姓名', '邮箱', '主页'])
        for each in department.run():
            print(each)
            ws.append(each)
    wb.save('professor_info/' + university + '.xlsx')
