import os
files = os.listdir('src/')

urls = input('ENTER PATH URLS: ')
url_o = open(urls,'r')
url_s = url_o.readlines()
url_o.close()
for s in url_s:
        for i in files:
                file = open('src/'+i,'r')
                fileter = file.read()
                file.close()
                param = s.find('?')
                if s[param+1:-1].strip() in fileter:
                        print(f'url -> {s.strip()} vulnirable -> {i}')

