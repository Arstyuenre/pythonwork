print('''        欢迎使用学生管理系统
         1.显示学生信息
         2.添加学生信息
         3.查询学生信息
         4.删除学生信息
         5.修改学生信息
         6.退出系统 ''')
students = [{'name':'su','ID': '001', 'score': '95'},
            {"name": "李四", "ID": "002", "score": "80"}]
while True:

    key = input("输入你想进行的操作:")
    if key == "1":
        for student in students:
            print(student)
    elif key == "2":
        name = input("请输入要添加的学生姓名")
        ID = input("请输入要添加的学生学号")
        score = input("请输入要添加的学生成绩")
        student = {"name": name,"ID": ID,"score": score}
        students.append(student)
    elif key == "3":
        name = input("请输入你要查询的学生姓名:")
        for student in students:
            if student["name"] == name:
                print(student)
    elif key == "4":
        name = input("请输入要删除的学生姓名:")
        for student in students:
            if student["name"] == name:
                students.remove(student)
    elif key == "5":
        name = input("请输入想要修改的学生姓名:")
        for student in students:
            if student["name"] == name:
                student["name"] = input('请输入修改后的名字:')
                student["ID"] = input("请输入修改后的学号:")
                student["score"] = input('请输入修改后的分数')
    elif key == "6":
        print("感谢使用本系统")
        break