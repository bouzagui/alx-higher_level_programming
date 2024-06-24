#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in rows:
        print(row)

    cursor.close()
    db.close()
