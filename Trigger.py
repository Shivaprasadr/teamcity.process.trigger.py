from xml.sax.saxutils import quoteattr
import requests
template = '<build><buildType id={id}/></build>'

url = "http://localhost:9090/httpAuth/app/rest/buildQueue/"
headers = {'Content-Type': 'application/xml'}
build_id = 'MyDeal_Mydealbuild1'
data = template.format(id=quoteattr(build_id))

r = requests.post(url, headers=headers, data=data, auth=("xxx", "123@xxx"), timeout=10)
print(r)