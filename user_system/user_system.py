# -*- coding: utf-8 -*-

# 用户登录系统
# 1. 用户信息保存在一个user_file里，name, password, email, intro
# 2. 文件的行数即为 用户的uid
# 3、用户可登录，用户可以修改信息， 修改需要验证密码
# 4、用户可以登出
# 5、用户可以删除自己， 需要验证密码
#
# 6、程序启动时读取全部用户



user_dict = {}
user_name_password = {}
login_list = []
current_index = 0
current_user = None


def init_user(name, password, uid=None, email=None, intro=None):
    return User(name, password, uid, email, intro)

def init_system():
    print "初始化数据"
    user_file = open('user_file.txt', 'r')
    global current_index
    for v in user_file.readlines():
        current_index += 1
        v = v.strip('\r\n')
        if v:
            v = v.split(',')
            uid = int(v[0])
            name = v[1]
            password = v[2]
            email = None
            intro = None
            if len(v) >= 4:
                email = v[3]
            if len(v) >= 5:
                intro = v[4]
            user_dict[uid] = init_user(name, password, uid, email, intro)
            user_name_password[name] = [uid, password]
    user_file.close()

def get_user_by_uid(uid):
    return user_dict[uid]


def validate(name, password):
    if name in user_name_password:
        if user_name_password[name][1] == password:
            return True, user_name_password[name][0]
        else:
            return False, None
    else:
        return True, None

def add_user_file(user):
    user_file = open('user_file.txt', 'a')
    global current_index
    current_index += 1
    write_list = [str(current_index), user.name, user.passward,
                  user.email or "", user.intro or ""]
    user_dict[current_index] = user
    user.uid = current_index
    user_file.write(','.join(write_list)+'\r\n')
    user_file.close()

def update_user_file(user):
    user_file = open('user_file.txt', 'r')
    pre_write = []
    for i, user_line in enumerate(user_file.readlines()):
        if i+1 == user.uid:
            write_list = [str(current_index), user.name, user.passward,
                  user.email or "", user.intro or ""]
            pre_write.append(','.join(write_list)+'\r\n')
        else:
            pre_write.append(user_line)
    user_file.close()
    if pre_write:
        user_file = open('user_file.txt', 'w')
        user_file.writelines(pre_write)
        user_file.close()

def delete_user_file(user):
    user_file = open('user_file.txt', 'r')
    pre_write = []
    for i, user_line in enumerate(user_file.readlines()):
        if i+1 == user.uid:
            pre_write.append('\r\n')
        else:
            pre_write.append(user_line)
    user_file.close()
    if pre_write:
        user_file = open('user_file.txt', 'w')
        user_file.writelines(pre_write)
        user_file.close()

class User(object):
    def __init__(self, name, password, uid=None, email=None, intro=None):
        self.name = name
        self.passward = password
        self.uid = uid
        self.email = email
        self.intro = intro

    def set_info(self, **kwargs):
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'intro' in kwargs:
            self.intro = kwargs['intro']

    def save(self):
        if self.uid:
            update_user_file(self)
        else:
            add_user_file(self)
        user_name_password[self.name] = [self.uid, self.passward]

    def delete(self):
        if self.uid:
            delete_user_file(self)
            user_dict.pop(self.uid)
            user_name_password.pop(self.name)
        else:
            pass

if __name__ == "__main__":
    init_system()
    while True:

        print '1: 登录 2: 退出系统'
        raw_input_a = raw_input('请输入（1 or 2）：')
        if raw_input_a == '1':
            current_user = None
            if not current_user:
                user = None
                name = raw_input('请出入用户名（如果是新用户会直接创建用户）：')
                password = raw_input('请出入密码：')
                validated, uid = validate(name, password)
                if validated and uid:
                    user = get_user_by_uid(uid)
                elif validated:
                    email = raw_input('请输入邮箱地址：')
                    intro = raw_input('请出入简介：')
                    user = User(name, password, email=email, intro=intro)
                    user.save()
                else:
                    print "用户名密码错误"
                current_user = user
            while current_user:
                print('1: 修改用户资料,  2:修改密码, 3: 退出登录, 4:删除用户')
                action = raw_input('请输入(1 or 2 or 3)：')
                if action == '1':
                    print '老邮箱地址:', current_user.email
                    email = raw_input('请输入新邮箱地址：')
                    print '老的简介:', current_user.intro
                    intro = raw_input('请输入新简介：')
                    if email or intro:
                        print '请验证密码'
                        password = raw_input('请出入密码：')
                        if current_user.passward == password:
                            if intro:
                                current_user.intro = intro
                            if email:
                                current_user.email = email
                            current_user.save()
                            print "保存成功"
                        else:
                            print "密码验证失败，保存失败"
                elif action == '2':
                    old_password = raw_input('旧的密码')
                    if current_user.passward == old_password:
                        password = raw_input('请输入新密码：')
                        if password == current_user.passward:
                            print "密码一样哟，不需要修改"
                        else:
                            current_user.password = password
                            current_user.save()
                            print "修改成功，请用新密码登录"
                            current_user = None
                    else:
                        print "密码验证失败"
                elif action == '3':
                    current_user = None
                elif action == '4':
                    confirm = raw_input('确认删除？(Y/N)：')
                    if confirm in 'Yy':
                        current_user.delete()
                        current_user = None
                    else:
                        pass
                else:
                    print '输入错误'
        elif raw_input_a == '2':
            break
        else:
            print '输入错误'