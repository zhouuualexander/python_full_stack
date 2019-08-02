'''
    学员信息管理系统
    1.学员信息数据源
    2.查看学员信息功能
    3.添加学员信息
    4.删除学员信息
    5.退出系统
    6.界面和交互
'''
# 1.学员信息数据
stu_list = [
    {'name': 'zhangsan', 'age': 20, 'classid': 'Python01'},
    {'name': 'lisi', 'age': 28, 'classid': 'Python02'},
    {'name': 'wangwu', 'age': 31, 'classid': 'Python03'}]
# 2.查看学员信息功能


def show_stus_info():
    """

    :return:
    """
    if len(stu_list) == 0:
        print('=' * 20, '没有学员信息', '=' * 20)
        return
    print(
        '|{0:<5}|{1:<10}|{2:<5}|{3:<10}|'.format(
            'sid',
            'name',
            'age',
            'classid'))
    print('-' * 40)
    for i, stu_dict in enumerate(stu_list):
        print(
            '|{0:<5}|{1:<10}|{2:<5}|{3:<10}|'.format(
                i + 1,
                stu_dict['name'],
                stu_dict['age'],
                stu_dict['classid']))

# 3.添加学员信息

def add_stu(name,age,classid):
    stu_dict = {'name': name, 'age': age, 'classid': classid}
    stu_list.append(stu_dict)
# 4.删除学员信息
def del_stu(sid):
    sid_int = int(sid)
    stu_list.pop(sid_int-1)
 #5.退出系统
def loginOut():
    pass
#6.界面和交互
while True:
    # 输出初始界面
    print('='*12,'学院管理系统','='*12)
    print('{0:1} {1:13} {2:15}'.format(' ','1.  查看学员信息','2. 添加学员信息'))
    print('{0:1} {1:13} {2:15}'.format(' ','3.  删除学员信息','4. 退出系统'))
    print('='*40)
    key = input('请输入对应的选择：')
    # 根据输入操作值，执行对应操作
    if key == '1':
        print('='*12,'学员信息浏览','='*12)
        show_stus_info()
        input('按回车继续：')

    elif key == '2':
        print('='*12,'添加学员信息','='*12)
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        classid = input('请输入班级号：')
        add_stu(name, age, classid)
        show_stus_info()
        input('按回车继续：')
    elif key == '3':
        print('='*12,'删除学员信息','='*12)
        show_stus_info()
        sid = input('请你输入要删除的学员的sid：')
        del_stu(sid)
        show_stus_info()
        input('按回车继续：')
    elif key == '4':
        loginOut()
        print('='*12,'再见','='*12)
        break
    else:
        print('='*12,'操作无效','='*12)
