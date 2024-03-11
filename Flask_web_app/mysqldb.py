import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MyNewPass",
        database="MBTAdb"
    )

    mycursor = mydb.cursor()
    
    # Modify the following line to include all the fields from the table
    sql = "INSERT INTO mbta_buses (id, latitude, longitude, vehicle_label, current_status, bearing, direction_id, occupancy_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    
    for mbtaDict in mbtaList:
    # Modify the following line to include all the fields from the table
        val = (mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], 
           mbtaDict['vehicle_label'], mbtaDict['current_status'], 
           mbtaDict['bearing'], mbtaDict['direction_id'], mbtaDict['occupancy_status'])
        
    mycursor.execute(sql, val)

    mydb.commit()