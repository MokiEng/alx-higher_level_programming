#!/usr/bin/pyhton3
'''
a python script that lists all cities
from the database hbtn_0e_4_usa.
'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    '''Create a cursor object to interact with the database.'''
    cur = db.cursor()
    '''Execute the SQL query to retrieve the cities.'''
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    '''Fetch all the results.'''
    rows = cur.fetchall()
    '''Display the results.'''
    for row in rows:
        print(row)
    '''Close the cursor and the connection.'''
    cur.close()
    db.close()
