import requests
import time
import numpy as np

##### get position of a single robot
get_URL = "http://localhost:1234/Vehicle/Position/XYZ/ALL"
get_req = requests.get(url=get_URL)


data = get_req.json()
print data

num_robot = len(data)
print(num_robot)



# ##### send target position of a single robot
# set_URL = "http://localhost:1234/Vehicle/Position/XYZ/Single"

# for i in range(num_robot):
#     xyz_data = {"id":i,"x":20*np.sin(i+1), "y":20*np.cos(i),"z":20*np.sin(i),"MovArgs":{"speed":10, "distThresh":1.0}}
# #lla_data = {"id":1,"data":{"lat":37.46832, "lon":-84.2317047,"alt":311.3}}

#     set_req = requests.post(url = set_URL, data = xyz_data)

set_URL = "http://localhost:1234/Vehicle/AddVelocity"
data = {"id":0,"x":0.3,"y":0.2,"z":0.3}
set_req = requests.request("POST",url = set_URL, data = data)


print set_req.status_code,'\n',set_req.reason

time.sleep(5)
set_req = requests.post(url = set_URL, data = data)
print set_req.status_code,'\n',set_req.reason


get_req = requests.get(url=get_URL)

data = get_req.json()
print data
