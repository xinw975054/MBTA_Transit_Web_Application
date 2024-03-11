import urllib.request
import json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # Modify the fields below based on the entries of your SQL table
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['vehicle_label'] = bus['attributes']['label']
            busDict['current_status'] = bus['attributes']['current_status']
            busDict['bearing'] = bus['attributes']['bearing']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']

            mbtaDictList.append(busDict)
    
    mysqldb.insertMBTARecord(mbtaDictList)

    return mbtaDictList
