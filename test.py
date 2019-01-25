import numpy as np

num_robots = 3

centroid = [2,4,4]
goal = []
for i in range(num_robots):
	temp = {}
	temp["id"] = i
	temp["x"] = centroid[0]
	temp["y"] = centroid[1]
	temp["z"] = centroid[2]
	goal.append(temp)

# xyz_data = {"id":0,"x":45.500, "y":72.3000,"z":10.000}
#lla_data = {"id":1,"data":{"lat":37.46832, "lon":-84.2317047,"alt":311.3}}
data_paras = {"positions":goal}
print(data_paras)

xyz_data = {"id":0,"x":45.500, "y":72.3000,"z":10.000}
xyz = {"positions":xyz_data}
print xyz