# -*- coding: utf-8 -*-

# 用户登录系统
# 1. 用户信息保存在一个user_file里，name, password, email, intro
# 2. 文件的行数即为 用户的uid
# 3、用户可登录，用户可以修改信息， 修改需要验证密码
# 4、用户可以登出
# 5、用户可以删除自己， 需要验证密码
# 6、程序启动时读取全部用户
#
# 作业： 补充新增用户，修改用户，删除用户时对文件的操作
# 选做题：写一个class User，使用User来记录每一条数据

class User(object):
    def __init__(self, uid, name, password, email, intro):
        self.uid = uid
        self.name = name
        self.password = password
        self.email = email
        self.intro = intro


user_password = {}
user_info = {} # key 用户id  value 用户信息
current_user = None
current_index = 0

def init_user_file():
    print "初始化数据"
    user_file = open('user_file.txt', 'r')
    global current_index
    # 遍历每一行
    for line in user_file.readlines():
        current_index += 1
        line = line.strip('\r\n')
        line = line.split(',')
        uid = int(line[0])
        name = line[1]
        password = line[2]
        # email = ??
        # intro = ??
        # user = User(uid, name, password, email, intro)
        # user_info[uid] = user
        # user.name
        user_info[uid] = line
        user_password[name] = [uid, password]
    pass


def update_user_info(email=None, intro=None, password=None):
    global current_user
    uid = int(current_user[0])
    if email:
        user_info[uid][3] = email
        # user_info[uid].email = email
    if intro:
        user_info[uid][4] = intro
    if password:
        user_info[uid][2] = password
        user_password[user_info[uid][1]] = [uid, password]
    # TODO:
    # 1、 open(file_name, 'r')
    # 2、 遍历每一行，找到要删除的一行，置为新的数据，不要忘了"\r\n"  file.close()
    # 3、 再把结果的数据写入这个文件 opne(file_name,'w')


def create_user(name, password, email, intro):
    global current_index
    current_index += 1
    user_info[current_index] = [str(current_index), name, password, email, intro]
    user_password[name] = [current_index, password]
    # TODO: 在文件末尾添加一条数据 open(file_nma, 'a')
    return current_index

def delete_user():
    global current_user
    uid = int(current_user[0])
    user = user_info.pop(uid)
    user_password.pop(user[1])
    # TODO:
    # 1、 open(file_name, 'r')
    # 2、 遍历每一行，找到要删除的一行，置为"\r\n"  file.close()
    # 3、 再把结果的数据写入这个文件 opne(file_name,'w')

def validate(name, password):
    if name in user_password:
        if user_password[name][1] == password:
            return True, user_password[name][0]
        else:
            return False, None
    else:
        return True, None

if __name__ == '__main__':
    init_user_file()
    while True:
        print "1: 登录， 2： 退出"
        choice = raw_input('请输入（1 ／ 2）:')
        if choice == '1':
            name = raw_input('请输入用户名：')
            password = raw_input('请输入密码')
            validated, uid = validate(name, password)
            if validated:
                if uid:
                    current_user = user_info[uid]
                else:
                    email = raw_input('请输入邮箱：')
                    intro = raw_input('请输入简介：')
                    uid = create_user(name, password, email, intro)
                    current_user = user_info[uid]
                print "登录成功"
            else:
                print "用户名或密码错误！！"
            while current_user:
                print "1: 修改用户资料， 2: 修改密码 3:退出登录 4: 删除用户"
                raw_input_a = raw_input("请输入（1/2/3/4）：")
                if raw_input_a == '1':
                    email = raw_input('请输入邮箱：')
                    intro = raw_input('请输入简介：')
                    password = raw_input('请输入密码')
                    if current_user[2] == password:
                        update_user_info(email=email, intro=intro)
                    else:
                        print '输入密码错误'
                if raw_input_a == '2':
                    password = raw_input('请输入旧密码')
                    if current_user[2] == password:
                        new_password = raw_input('请输入新密码')
                        update_user_info(password=new_password)
                        current_user = None
                    else:
                        print '输入密码错误'
                if raw_input_a == '3':
                    current_user = None
                if raw_input_a == '4':
                    delete_user()
                    current_user = None
        elif choice == '2':
            print "退出系统"
            break
        else:
            print "输入错误，请重新输入"