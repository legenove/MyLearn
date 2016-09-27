import os,datetime
from os.path import join, getsize
from load_data import mp3_file

mp3_file_path = mp3_file # "/Users/legenove/GuokrWorkSpace/Other/mp3_files/"
def remove_mp3s():
    for root, dirs, files in os.walk(mp3_file_path):
        for name in files:
            if name.endswith(".mp3"):
                if getsize(join(root, name)) / 1024 < 0.5:
                    if os.path.exists(join(root, name)):
                        os.remove(join(root, name))
def get_all_size():
    return sum([getsize(mp3_file_path+x) for x in os.listdir(os.path.dirname(mp3_file_path))])

def get_mp3s_num():
    return len([x for x in os.listdir(os.path.dirname(mp3_file_path))])

def get_files_num():
    return sum([len(os.listdir(os.path.dirname(x))) for x in ['./'+x+'/' for x in os.listdir(os.path.dirname('./'))]])

if __name__ == '__main__':
    # remove_mp3s()
    print get_mp3s_num()
    print datetime.datetime.now()
    # print get_all_size()

# sum([len(os.listdir(os.path.dirname(x))) for x in ['./'+x+'/' for x in os.listdir(os.path.dirname('./'))]])