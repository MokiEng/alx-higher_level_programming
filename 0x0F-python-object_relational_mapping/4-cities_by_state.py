#!/usr/bin/pyhton3
'''
a python script that lists all cities
from the database hbtn_0e_4_usa.
'''
import MySQLdb
import sys


def list_cities(username, password, database):
    '''Connect to MySQL server.'''
    try:
        conn = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database)
    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)

    '''Create a cursor object to interact with the database.'''
    cursor = conn.cursor()

    '''Execute the SQL query to retrieve the cities.'''
    query = "SELECT * FROM cities ORDER BY cities.id ASC"
    try:
        cursor.execute(query)
    except MySQLdb.Error as e:
        print("Error executing the query: {}".format(e))
        sys.exit(1)

    '''Fetch all the results.'''
    results = cursor.fetchall()

    '''Close the cursor and the connection.'''
    cursor.close()
    conn.close()

    '''Display the results.'''
    for row in results:
        print(row)


'''
Check if the script is run directly and gather the command-line arguments.
'''
if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    '''Call the function to list cities.'''
    list_cities(username, password, database)
