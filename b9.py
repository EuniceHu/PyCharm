import requests

r = requests.get('http://k18-bigdata-cas.ceiec.com/cas/login?service=http://K18-BigData.CEIEC.com/api/SystemManager/shiro-cas&locale=zh_CN')
print(r.text)
