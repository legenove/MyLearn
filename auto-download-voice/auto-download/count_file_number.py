import os,time
from os.path import join, getsize
mp3_file_path =  "/Users/legenove/GuokrWorkSpace/Other/mp3_files/"
def remove_mp3s():
    for root, dirs, files in os.walk(mp3_file_path):
        print root, dirs, files
        for name in files:
            if name.endswith(".mp3"):
                if getsize(join(root, name)) / 1024 < 0.5:
                    if os.path.exists(join(root, name)):
                        print join(root, name)
                        os.remove(join(root, name))
def get_mp3s_num():
    return len([x for x in os.listdir(os.path.dirname(mp3_file_path))])

if __name__ == '__main__':
    # remove_mp3s()
    print get_mp3s_num()

