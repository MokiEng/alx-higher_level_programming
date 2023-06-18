#!/usr/bin/pyhton3
'''
a python script that lists all cities
from the database hbtn_0e_4_usa.
'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    '''Create a cursor object to interact with the database.'''
    cur = db.cursor()
    '''Execute the SQL query to retrieve the cities.'''
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    '''Fetch all the results.'''
    rows = cur.fetchall()
    '''Display the results.'''
    for row in rows:
        print(row)
    '''Close the cursor and the database'''
    cur.close()
    db.close()
