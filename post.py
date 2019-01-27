import requests
r = requests.post("http://localhost:1234/Vehicle/Position/LLA/Multi", data={
    "positions":[
        {
                "id":0, 
                "data":{
                        "lat": 37.46797,
                        "lon": -84.23042,
                        "alt": 270.082184
                                
                    }
                    
            },
        {
                 "id":1, 
                 "data":{
                         "lat": 37.46697,
                         "lon": -84.23042,
                         "alt": 270.082184
                                 
                     }
                     
            }, 
        {
                 "id":2, 
                 "data":{
                         "lat": 37.46597,
                         "lon": -84.23042,
                         "alt": 270.082184
                                 
                     }
                     
            },
        {
                 "id":3, 
                 "data":{
                         "lat": 37.46497,
                         "lon": -84.23042,
                         "alt": 270.082184
                                 
                     }
                     
            },
        {
                 "id":4, 
                 "data":{
                         "lat": 37.46397,
                         "lon": -84.23042,
                         "alt": 270.082184
                                 
                     }
                     
            }
          
        ],
        "MovArgs":{"speed":5,"distThresh":1.4}
    })
print(r.status_code, r.reason)
