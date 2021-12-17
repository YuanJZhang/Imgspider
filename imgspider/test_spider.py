import requests

url = 'http://imgfzone.tooopen.com/20211125/tooopen_s135134513417553.jpg'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}

try:
    r = requests.get(url,headers=headers)
    print(r.text())
    r_code = r.status_code
    print(url,"访问状态",r_code)

except:
    print('wangluoduankai')