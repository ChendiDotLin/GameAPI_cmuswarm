import requests
import time
import numpy as np


##### parameters
connectivity_radius = 20.0
max_linear_velocity = 2.0

##### get position of all robots
get_URL = "http://localhost:1234/Vehicle/Position/XYZ/ALL"
get_req = requests.get(url=get_URL)


p_data = get_req.json()
print p_data
num_robots = len(p_data)
print num_robots

positions = []
for i in range(num_robots):
	positions.append([p_data[i][u'x'],p_data[i][u'y'],p_data[i][u'z']])
centroid = sum(np.array(positions))/3





##### send target position of all robots
set_URL = "http://localhost:1234/Vehicle/Position/XYZ/Multi"
goal = []
for i in range(num_robots):
	goal.append({"id":i,"MovArgs":{"speed":10,"distThresh":1.0},"X":centroid[0],"Y":centroid[1],"Z":centroid[2]})

# xyz_data = {"id":0,"x":45.500, "y":72.3000,"z":10.000}
	# data = {"id":i,"x":centroid[0], "y":centroid[1],"z":centroid[2]}

#lla_data = {"id":1,"data":{"lat":37.46832, "lon":-84.2317047,"alt":311.3}}
data_paras = {"positions":data}
print(data_paras)
set_req = requests.post(url = set_URL, data = data_paras)
print set_req.status_code,'\n',set_req.reason

time.sleep(5)

get_req = requests.get(url=get_URL)

data = get_req.json()
print data

velocities = [[0,0,0]]*num_robots
print velocities
# while True:
# 	for i in range(num_robots):
		# i is the id of each robot
		