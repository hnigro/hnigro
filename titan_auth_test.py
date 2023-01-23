import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

session = requests.Session()

titan_login = session.post("http://10.177.30.4/api/v1/system/information/login", json={
	"user": "Administrator",
	"password": "TitanLive@At3me"
	}, verify = False)

print("Login {}".format(titan_login))
#print(titan_login.cookies)

device_info = session.get("http://10.177.30.4/api/v1/system/information/version")

print("Version {}".format(device_info.content))

