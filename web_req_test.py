import requests
import time

##### get position of a single robot
get_URL = "http://localhost:1234/Vehicle/Position/XYZ/index=0"
get_req = requests.get(url=get_URL)


data = get_req.json()
print data




##### send target position of a single robot
set_URL = "http://localhost:1234/Vehicle/Position/XYZ/Single"

xyz_data = {"id":0,"x":45.500, "y":72.3000,"z":10.000}
#lla_data = {"id":1,"data":{"lat":37.46832, "lon":-84.2317047,"alt":311.3}}

set_req = requests.post(url = set_URL, data = xyz_data)
print set_req.status_code,'\n',set_req.reason

time.sleep(5)

get_req = requests.get(url=get_URL)

data = get_req.json()
print data
