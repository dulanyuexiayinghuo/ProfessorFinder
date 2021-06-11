import os
import openpyxl


def check():
    dst = 'professor_info'
    if not os.path.isdir(dst):
        os.mkdir(dst)


def write_excel(uni_departments):
    wb = openpyxl.Workbook()
    university = tuple(uni_departments.keys())[0]
    for department, ok in uni_departments.items():
        if ok:
            department = department()
            print('processing: ' + university + department.name)
            ws = wb.create_sheet(department.name, 0)
            ws.append(['学校', '院系', '姓名', '邮箱', '主页'])
            for each in department.run():
                ws.append(each)
    wb.save('professor_info/' + university + '.xlsx')
