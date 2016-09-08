# -*-coding:utf-8-*-
import urllib2
import json
import sys
import time

# see http://wiki.1verge.net/webdev:ds:show
API_FMT = "http://10.103.88.54/show.show?q=exclusive:1&fd=showcategory+firstepisode_videourl+showname+tudou_num&pn=%d&pl=100&ob=showweek_vv:desc&ft=json"


def shows():
    page = 1
    shows = []
    while True:
        try:
            data = json.load(urllib2.urlopen(API_FMT % page))
        except:
            time.sleep(1)
            try:
                data = json.load(urllib2.urlopen(API_FMT % page))
            except:
                data = {'results': ""}

        if len(data['results']) == 0:
            break
        shows.extend(data['results'])
        page += 1
    return shows


def gen(shows_info, white_ids=None):
    data = []
    shows_info.sort(key=lambda x: x['tudou_num'])
    if white_ids is None:
        for show in shows_info:
            if 'firstepisode_videourl' not in show:
                print >> sys.stderr, "忽略<%s>, showid:%s, 似乎还没有正片.. " % (show[
                                                                            "showname"].encode("utf8"),
                                                                        show['showid'].encode("utf8"))
                continue
            data.append({
                "id": show['tudou_num'],
                "type": "show",
                "skip_inf": {
                    "skip_type": "yk_video",
                    "browser_type": 1,
                    "skip_url": str(show["firstepisode_videourl"]).replace('/v_show/', '/video/').replace('v.youku',
                                                                                                          'm.youku') + '?from=tudouapp',
                    "yk_play": "youku://play?showid=%s&source=app-tudou" % show["showid"],
                    "yk_play_ios": "youku://play?vid=%s&source=app-tudou" % show["showid"],
                }
            })
    else:
        show_id = 0
        for num in range(len(white_ids)):
            while white_ids[num] > int(shows_info[show_id]['tudou_num']):
                show_id += 1
            if num == 18:
                pass
            if white_ids[num] == int(shows_info[show_id]['tudou_num']):
                if 'firstepisode_videourl' not in shows_info[show_id]:
                    print >> sys.stderr, "忽略<%s>, showid:%s, 似乎还没有正片.. " % (shows_info[show_id][
                                                                                "showname"].encode("utf8"),
                                                                            shows_info[show_id]['showid'].encode(
                                                                                "utf8"))
                    print str(num) + ":" + str(white_ids[num])
                    continue
                data.append({
                    "id": shows_info[show_id]['tudou_num'],
                    "type": "show",
                    "skip_inf": {
                        "skip_type": "yk_video",
                        "browser_type": 1,
                        "skip_url": str(shows_info[show_id]["firstepisode_videourl"]).replace('/v_show/',
                                                                                              '/video/').replace(
                            'v.youku',
                            'm.youku') + '?from=tudouapp',
                        "yk_play": "youku://play?showid=%s&source=app-tudou" % shows_info[show_id]["showid"],
                        "yk_play_ios": "youku://play?vid=%s&source=app-tudou" % shows_info[show_id]["showid"],
                    }
                })
            else:
                print str(num) + ":" + str(white_ids[num])
                continue
    return data


def get_white_ids(_file_name):
    _file = open(_file_name, 'r')
    ids = []
    for l in _file.readlines():
        ids.append(int(l.split()[1].strip()))
    ids.sort()
    return ids


def main():
    ids = None
    ids = get_white_ids('show_whites.txt')
    a = open('show_android_all.txt', 'w')
    a.write(json.dumps(gen(shows(), ids), indent=2))
    a.save()
    a.close()
    print ids


if __name__ == "__main__":
    main()
