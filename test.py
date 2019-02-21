import requests
import time
import numpy as np
import json

##### parameters
connectivity_radius = 20.0
max_linear_velocity = 2.0

##### get position of all robots
get_URL = "http://localhost:1234/Vehicle/Position/XYZ/ALL"
get_req = requests.get(url=get_URL)


p_data = get_req.json()
print (p_data)
num_robots = len(p_data)
print (num_robots)

positions = []
for i in range(num_robots):
	positions.append([p_data[i][u'x'],p_data[i][u'y'],p_data[i][u'z']])
centroid = sum(np.array(positions))/num_robots

connectivity_radius = 10




##### send target position of all robots
set_URL = "http://localhost:1234/Vehicle/Position/XYZ/Multi"
# set_URL = "http://localhost:1234/Vehicle/Position/LLA/Multi"
goal = []

dt = 2
t = 0

while (t <40):
	goal = []

	get_req = requests.get(url=get_URL)


	p_data = get_req.json()
	print (p_data)
	num_robots = len(p_data)
	print (num_robots)

	positions = []
	for i in range(num_robots):
		positions.append([p_data[i][u'x'],p_data[i][u'y'],p_data[i][u'z']])
	centroid = sum(np.array(positions))/num_robots


	for i in range(num_robots):
		positions = []
		n = 0
		i_pos = np.array([p_data[i][u'x'],p_data[i][u'y'],p_data[i][u'z']])
		for j in range(num_robots):
			if (j!=i):
				j_pos = np.array([p_data[j][u'x'],p_data[j][u'y'],p_data[j][u'z']])
				if (np.linalg.norm(i_pos - j_pos) < connectivity_radius):
					positions.append(j_pos)
					n = n + 1
		if (n!=0):
			centroid = sum(np.array(positions))/n
		else:
			centrod = i_pos
		print(centroid)
		goal.append({"id":i,"x":centroid[0],"y":centroid[1],"z":centroid[2]})
		# a = '{"id":'+str(i)+',"x":22,"y":33,"z":44}'
		# print(type(a))
		# print(a)
		# b = json.loads(a)
		# goal.append(b)

		# goal.append({"id":i,"data":{"lat":37,"lon":-84,"alt":270}})
		# goal.append({"id":i,"MovArgs":{"speed":10,"distThresh":1.0},"x":centroid[0],"y":centroid[1],"z":centroid[2]})

	# xyz_data = {"id":0,"x":45.500, "y":72.3000,"z":10.000}
		# data = {"id":i,"x":centroid[0], "y":centroid[1],"z":centroid[2]}
		# print i
	#lla_data = {"id":1,"data":{"lat":37.46832, "lon":-84.2317047,"alt":311.3}}
	# goal = '[{"id:0","x":22,"y":33,"z":44},{"id:1","x":22,"y":33,"z":44},{"id:2","x":22,"y":33,"z":44}]'
	# goaly = json.loads("goal")

	margs = {"speed":0.1, "distThresh":1}
	data_paras = {"positions":goal,"MovArgs":margs}
	# data_paras = json.dumps(data_paras)
	# print(data_paras["positions"][0])
	# print(data_paras["MovArgs"])
	print (data_paras)
	print(type(data_paras))
	# data_paras = json.dumps(data_paras)
	# data_paras = {"positions":[{"id":0, "MovArgs":{"speed":10, "distThresh":1.0}, "X":309.29, "Y":354, "Z":-107},{"id":1, "MovArgs":{"speed":5, "distThresh":1.0},"X":406,  "Y":354, "Z":-230}, {"id":2, "MovArgs":{"speed":20, "distThresh":1.0},  "X":358,  "Y":374,  "Z":-351}]}
		# print(data)
	set_req = requests.request("POST",url = set_URL, json = data_paras)

	time.sleep(dt)

	set_req = requests.request("POST",url = set_URL, json = data_paras)

	print (set_req.status_code,'\n',set_req.reason)
	# set_req = requests.post(url = set_URL, data = data)
	# print set_req.status_code,'\n',set_req.reason
	t = t + 2*dt
	time.sleep(dt)
