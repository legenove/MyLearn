# -*-coding:utf-8-*-
import urllib2
import json
import sys
import time


def gen(shows_info):
    data = []
    for show in shows_info:
        data.append({
            "id": show[0],
            "type": "show",
            "skip_inf": {
                "skip_type": "yk_video",
                "browser_type": 1,
                "skip_url": str(show[3]).replace('/v_show/', '/video/').replace('v.youku',
                                                                                  'm.youku') + '?from=tudouapp',
                "yk_play": "youku://play?showid=%s&source=app-tudou" % show[2],
                "yk_play_ios": "youku://play?vid=%s&source=app-tudou" % show[2],
            }
        })
    return data


def get_white_ids(_file_name):
    _file = open(_file_name, 'r')
    ids = []
    for l in _file.readlines():
        print l
        ids.append((
        int(l.split('\t')[3].replace('\xc2\xa0', '').strip()), l.split('\t')[2].replace('\xc2\xa0', '').strip(),
        l.split('\t')[5].replace('\xc2\xa0', '').strip()))
    ids.sort(key=lambda x: x[0])
    return ids


def main():
    ids = None
    ids = get_white_ids('whiteids_has_url.txt')

    print ids


if __name__ == "__main__":
    main()
