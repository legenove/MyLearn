__author__ = 'legenove'
import urllib

f = open('bilihtml', 'r')
img_url = []
for line in f:
    fist = line.find("http://")
    end = line.find(".jpg")
    if fist > 0 and end > 0:
        img_url.append(line[fist:end+4])

print img_url

path = "img/"
i = 0
for url in img_url:
    print i
    name = url.split('/')[-1]
    data = urllib.urlopen(url).read()
    f = file(path+str(i)+'_'+name, "wb")
    f.write(data)
    f.close()
    i += 1