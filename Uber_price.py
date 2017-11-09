import pandas as pd 
import requests
import datetime
import time
import os.path
import json
import numpy as np

headers = {'Authorization' : 'Token FwvxDLWAYsKuxe-e_Da-Aq4_pj44suAXiOnszStO'}
df = pd.read_csv('E:/Saket/Project/NYC/Uber_feb/Uber_data_pull_21_feb/Uber_req_21_feb.csv', header=None)
start_Lat = df[0][1:60]
start_Lon = df[1][1:60]
end_Lat = df[2][1:60]
end_Lon = df[3][1:60]


# Conversion from Panda Series to Numpy array
start_Lat = start_Lat.values
start_Lon = start_Lon.values
end_Lat = end_Lat.values
end_Lon = end_Lon.values

# Number of cities
n_start = start_Lat.size
n_end = end_Lat.size


for t in range(0,289):
    for c1 in range(0,59):
        for c2 in range(0,1):      
            start_latitude = str(start_Lat[c1])# Iterate over the locations and find the distances
            start_longitude = str(start_Lon[c1])
            end_latitude = str(end_Lat[c2])
            end_longitude = str(end_Lon[c2])
            payload = {'start_latitude': start_latitude, 'start_longitude': start_longitude, 'end_latitude' : end_latitude, 'end_longitude' : end_longitude}
            requests.packages.urllib3.disable_warnings()
            resp = requests.get('https://api.uber.com/v1.2/estimates/price', headers=headers, params=payload, verify=False,timeout=12)
            resp = json.loads(resp.text)
            if resp =={"message":"No authentication provided.","code":"unauthorized"}:
                print("No Authentication provided")
                continue
            for i in range(len(resp["prices"])):
                resp["prices"][i]["time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                resp["prices"][i]["s_lat"] = start_latitude
                resp["prices"][i]["s_long"] = start_longitude
                resp["prices"][i]["e_lat"] = end_latitude
                resp["prices"][i]["e_long"] = end_longitude
            save_path = 'E:/Saket/Project/NYC/Uber_feb/Uber_data_pull_23_feb/Price_data'
            name_of_file = (str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
            completeName = os.path.join(save_path,name_of_file+".json")         
            file1 = open(completeName, "w")
            toFile = str(resp)
            file1.write(toFile)
            file1.close()        
    
    time.sleep(150)