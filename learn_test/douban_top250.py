#! -*- coding: utf-8 -*-

import time
import urllib2
from bs4 import BeautifulSoup as bs

# URLS = []
URLS = ['https://movie.douban.com/subject/1292052/']
TOP250_URL = 'https://movie.douban.com/top250'

import psycopg2

db_setting = {
    'host': '10.0.80.13',
    'port': 5432,
    'user': 'study_group',
    'password': 'ssss',
    'database': 'douban',
}

conn = psycopg2.connect(host='10.0.80.13',
                        user='study_group',
                        password='ssss',
                        database='douban',
                        port=5432)


def get_html(url):
    resp = urllib2.urlopen(url)
    html = resp.read()
    return html


def extract_data(info, data):
    attrs = info.find_all('span', class_='attrs')
    # 导演数据
    print(attrs)
    if len(attrs) == 1:
        attrs = attrs + [None, None]
    elif len(attrs) == 2:
        attrs.append(None)
    directors, playwrights, casts = attrs
    directors = directors.find_all('a')
    directors_info = []
    for director in directors:
        directors_info.append((director.text, director.get('href')))
    data['directors'] = directors_info
    # 编剧数据
    playwrights_info = []
    if playwrights:
        playwrights = playwrights.find_all('a')
        for playwright in playwrights:
            playwrights_info.append((playwright.text, playwright.get('href')))
    data['playwrights'] = playwrights_info
    # 主演数据
    casts_info = []
    if casts:
        casts = casts.find_all('a')
        for cast in casts:
            casts_info.append((cast.text, cast.get('href')))
    data['casts'] = casts_info
    keys = ['genres', ]
    # 其它信息
    infos = info.text.split('\n')
    infos = filter(None, infos)
    genres_info, region_info, language_info, _, length_info = infos[3:8]
    for i, info in enumerate(infos):
        if u'类型' in info:
            genres_info = info
        elif u'制片国家' in info:
            region_info = info
        elif u'片长' in info:
            length_info = info
            print(length_info)
        elif u'语言' in info:
            language_info = info
    genres = genres_info.split(':')[1].split('/')
    data['genres'] = genres
    region = region_info.split(':')[1]
    data['region'] = region
    language = language_info.split(':')[1]
    data['language'] = language
    import re

    nums = re.findall(r'\d+', length_info)
    data['length'] = nums[0] if nums else 0
    print(data)
    return data


def parse_movie(html):
    data = {}
    soup = bs(html, "lxml")
    content = soup.find(id="content")
    h1 = content.h1.span.text
    data['title'] = h1
    print h1
    year = content.h1.find('span', class_='year').text
    data['score'] = (content
                     .find('div', id='interest_sectl')
                     .find('strong', class_="ll rating_num")
                     .text)
    try:
        data['summary'] = u"。".join(
            [s.strip() for s in (content
                                 .find('div', id='link-report')
                                 .find('span', class_='short')
                                 .find('span').text).split('\n') if s])
    except:
        data['summary'] = u"。".join(
            [s.strip() for s in (content
                                 .find('div', id='link-report')
                                 .find('span').text).split('\n') if s])
    data['year'] = year
    info = content.find('div', id='info')
    _data = extract_data(info, data)
    return _data


def parse_top250(html):
    soup = bs(html, "lxml")
    content = soup.find(id="content")
    lis = content.ol.find_all('li')
    for li in lis[:]:
        url = li.find(class_='hd').a.get('href')
        URLS.append(url)
    next = content.find('div', class_='paginator').find('span', class_='next').a
    if next:
        next_url = '%s%s' % (TOP250_URL, next.get('href'))

        next_html = get_html(next_url)
        parse_top250(next_html)


def main():
    html = get_html(TOP250_URL)
    parse_top250(html)
    # print URLS
    for url in URLS[233:]:
        time.sleep(1)
        try:
            movie_html = get_html(url)
            print url
            data = parse_movie(movie_html)
            write_into_db(data, url)
        except urllib2.HTTPError:
            pass


def write_into_db(data, url):
    director = data.get('directors')[0]
    casts = data.get('casts')
    language = data.get('language')
    genres = data.get('genres')
    region = data.get('region')
    director_id = get_celebrity_id(director[0])
    cast_ids = []
    type_ids = []
    for cast in casts:
        cast_ids.append(get_celebrity_id(cast[0]))
    language_id = get_language_id(language)
    nation_id = get_nation_id(region)
    for genre in genres:
        type_ids.append(get_type_id(genre))
    movie_id = get_movie(data.get('title'), data.get('year'), language_id,
                         director_id, nation_id, type_ids[0],
                         data.get('length'), data.get('summary'),
                         score=data.get('score', 0), douban_link=url)
    print movie_id
    for cast_id in cast_ids:
        set_movie_actor(movie_id, cast_id)


def get_celebrity_id(name):
    return get_model_id('celebrity', name)


def get_language_id(name):
    return get_model_id('language', name)


def get_nation_id(name):
    return get_model_id('nation', name)


def get_type_id(name):
    return get_model_id('type', name)


def get_model_id(model_name, name):
    name = name.replace("'", "''")

    cur = conn.cursor()

    cur.execute("select id from %s where name = '%s';" % (model_name, name))

    res = cur.fetchone()

    if not res:
        cur.execute("select count(*) from %s;" % model_name)
        count = cur.fetchone()
        cur.execute("insert into %s (id, name) values (%s,'%s')" % (
            model_name, int(count[0] + 1), name))
        cur.execute("select id from %s where name = '%s';" % (model_name, name))
        res = cur.fetchone()
        conn.commit()
    cur.close()
    return res[0]


def get_movie(title, year, language_id, director_id, nation_id, type_id, length,
              summary, rank=0, score=0, imdb_link="", douban_link=""):
    title = title.replace("'", "''")
    summary = summary.replace("'", "''")
    cur = conn.cursor()
    cur.execute("select id from movie where name = '%s';" % title)
    res = cur.fetchone()
    if not res:
        cur.execute("select count(*) from movie;")
        count = cur.fetchone()
        print(year, length, score)
        print(
        (int(count[0] + 1)), title, int(year[1:-1]), language_id, director_id,
        nation_id, type_id, int(length), summary, rank, float(score), imdb_link,
        douban_link)
        args = "(%s, '%s',  %s, %s,  %s,  %s,   %s, %s, '%s', %s, %s,'%s', '%s')" % (
        (int(count[0] + 1)), title, int(year[1:-1]), language_id, director_id,
        nation_id, type_id, int(length), summary, rank, float(score), imdb_link,
        douban_link)
        cur.execute(
            'insert into movie (id, "name", publish_year, language_id, directo'
            'r_id, nation_id, type_id, "length", summary, douban_rank, douban_'
            'score, imdb_link, douban_link) values ' + args)
        cur.execute("select id from movie where name = '%s';" % title)
        res = cur.fetchone()
        conn.commit()
    cur.close()
    return res[0]


def set_movie_actor(movie_id, actor_id):
    cur = conn.cursor()
    cur.execute(
        "select * from movie_actor where movie_id = %s and actor_id = %s;" % (
        movie_id, actor_id))
    res = cur.fetchone()
    if not res:
        cur.execute(
            "insert into movie_actor (movie_id, actor_id) values (%s, %s)" % (
            movie_id, actor_id))
        conn.commit()
    cur.close()


if __name__ == '__main__':
    main()


