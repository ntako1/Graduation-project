import mysql.connector

def insert_into_db(data):
    print(data)  # Print the received data for debugging purposes

    # cnx = mysql.connector.connect(user='root', password='',
    #                               host='localhost', database='arduino_data')

    cnx = mysql.connector.connect(user='admin', password='whlIGQW4',
                                  host='mysql-158812-0.cloudclusters.net',port='10014', database='arduino_data')  

    cursor = cnx.cursor()

  
   

    try:
        # Notice 'id' is no longer included here
        query = ("INSERT INTO info_data"
                 "(Humidity, Temperature, AirQuality, WaterLevel, Soil_Condition, Light) "
                 "VALUES (%s, %s, %s, %s, %s, %s)")

        # execute the query with the provided data
        cursor.execute(query, data)

        # Make sure data is committed to the database
        cnx.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        cnx.close()
