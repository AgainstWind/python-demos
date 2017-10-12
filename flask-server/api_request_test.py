import requests

urll = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(urll)

#print r.headers()
print '**************************'
print r.status_code
print '*************************'
response_dict = r.json()
print response_dict