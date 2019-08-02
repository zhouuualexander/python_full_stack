import random
"""
    ATM系统
    1.账户信息数据
    2.登录/注册
    3.查询余额
    4.取钱
    5.存钱
    6.退出
    7.界面和交互
"""
# 1. 账户信息数据
user_info = [
    {'cid': '289907708299758165',
     'password': '989979',
     'name': 'Tom',
     'balance': 1000},
    {'cid': '219107208199758165', 'password': '837998',
        'name': 'Jerry', 'balance': 193939},
    {'cid': '289907231299753332', 'password': '213121', 'name': 'Atom', 'balance': 3},
    {'cid': '289322121299752332', 'password': '116611',
        'name': 'Alex', 'balance': 123323232323232323}
]
# 2. 登录/注册


def login_regi(user_cid):
    """
    输入卡号和密码，如果卡号和密码匹配，即可登录，否则将引导用户进行注册新卡
    :param user_cid: 用户卡号
    """
    info_valid = False  # 默认信息验证失败，准备验证
    password_count = 5  # 密码剩余尝试输入次数
    need_new_cid = False  # 默认不需要注册新卡
    while not info_valid:  # 如果没验证，即可开始验证用户名及密码是否匹配
        for user in user_info:
            if user_cid == user['cid']:
                password_count = password_count - 1
                user_password = input('请输入密码:')
                # 如果密码错误并且还有剩余尝试次数，继续引导用户输入密码
                while user_password != user['password'] and password_count > 0:
                    user_password = input(
                        '密码错误，请重新输入密码' + '（还有' + str(password_count) + '次机会' + '）：')
                    password_count = password_count - 1
                if user_password == user['password'] and password_count >= 0:
                    print('登陆成功！')
                    cid = user['cid']
                    return cid
                else:
                    print('密码输入次数已用完，为了您的保障账户安全，请到柜台办理解卡手续，谢谢。')
                info_valid = True  # 信息验证完毕，用户办理手续
        if not info_valid:  # 如果卡号信息有误
            need_new_cid = True  # 需要注册新卡
        info_valid = True  # 信息核对完毕

    if need_new_cid:
        print("没有此卡号，请问您是否需要办理一张银行卡")
        answer = input("需要请输入数字1，不需要请输入其他数字：")
        set_password_finished = False
        if answer == '1':
            user_info_dic = {'cid': str(
                random.randint(
                    200000000000000000,
                    300000000000000000)), 'name': input("请输入您的姓名拼音：")}

            while not set_password_finished:
                password_1 = input("请输入6位数字密码：")
                if len(password_1) != 6:
                    print("您只能输入6位密码")
                elif len(password_1) == 6:
                    password_2 = input("请再次输入6位密码：")
                    if password_1 == password_2:
                        user_info_dic['password'] = password_2
                        set_password_finished = True

                    else:
                        print("您第二次输入的密码与第一次不相符，请重试")
            user_info_dic['balance'] = 0
            cid = user_info_dic['cid']
            user_info.append(user_info_dic)

            return cid
        else:
            print("感谢使用本ATM机，欢迎下次再来。")

# 3.查询余额


def show_user_balance(cid):

    print(
        '|{0:<20}|{1:<20}|{2:<20}|'.format(
            'cid',
            'name',
            'balance'))
    for user in user_info:
        if user['cid'] == cid:
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    user['cid'],
                    user['name'],
                    user['balance']))
            return cid
# 4.取钱


def withdraw_money(cid):
    for user in user_info:
        if user['cid'] == cid:
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    'cid',
                    'name',
                    'balance'))
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    user['cid'],
                    user['name'],
                    user['balance']))
    quantity = int(input("请问您需要取多少钱？"))
    valid = False
    while not valid:
        for user in user_info:
            if user['cid'] == cid:
                if 0 <= quantity <= user['balance']:
                    user['balance'] = user['balance'] - quantity
                    print(
                        '|{0:<20}|{1:<20}|{2:<20}|'.format(
                            'cid',
                            'name',
                            'balance'))
                    print(
                        '|{0:<20}|{1:<20}|{2:<20}|'.format(
                            user['cid'],
                            user['name'],
                            user['balance']))
                    valid = True
                    return cid
                else:
                    quantity = int(input("对不起，您的余额不足, 请重新输入："))
# 5.存钱


def deposit(cid):

    for user in user_info:
        if user['cid'] == cid:
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    'cid',
                    'name',
                    'balance'))
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    user['cid'],
                    user['name'],
                    user['balance']))
    quantity = int(input("请问您需要存多少钱？"))
    for user in user_info:
        if user['cid'] == cid:
            user['balance'] = user['balance'] + quantity
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    'cid',
                    'name',
                    'balance'))
            print(
                '|{0:<20}|{1:<20}|{2:<20}|'.format(
                    user['cid'],
                    user['name'],
                    user['balance']))
            return cid
# 6.退出


def logout():
    pass
# 7.交互界面


def user_interface():
    print("=" * 20, '欢迎使用本ATM机', "=" * 20)
    user_cid = input('请输入您的卡号：')
    cid = login_regi(user_cid)
    while True:
        print('{0:1} {1:13} {2:15}'.format(' ', '1.  查看余额', '2. 取钱'))
        print('{0:1} {1:13} {2:15}'.format(' ', '3.  存钱', '4. 退出系统'))
        print('=' * 60)
        key = input('请输入对应的选择：')
        # 根据输入操作值，执行对应操作
        if key == '1':
            print('=' * 12, '查看余额', '=' * 12)
            cid = show_user_balance(cid)
            input('按回车继续：')

        elif key == '2':
            print('=' * 12, '取钱', '=' * 12)
            cid = withdraw_money(cid)
            input('按回车继续：')
        elif key == '3':
            print('=' * 12, '存钱', '=' * 12)
            deposit(cid)
            input('按回车继续：')
        elif key == '4':
            logout()
            print('=' * 22, '再见', '=' * 22)
            break
        else:
            print('=' * 12, '操作无效', '=' * 12)


user_interface()
