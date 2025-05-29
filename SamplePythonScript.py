import os
import sys
import psycopg2
from pprint import pprint
# Local imports.  SierraDB.py would be in a common folder used by all similar Python scripts,
# while SQL.py resides in the same folder as this Python script (basedir).
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, basedir + '/../pymodules')
sys.path.insert(0, basedir)




db_host = "my-sierra-db.iii.com"
port = "1032"
sierra_database = "iii"
sierra_user = "my-sierra-user"
sierra_user_password = "my-sierra-user-password"




sql_query = """
    SET search_path = 'sierra_view';
    SELECT
        code AS "Location Code",
        name AS "Location Name"
    FROM location_myuser
    ORDER BY
        "Location Code" DESC
    LIMIT 15
    ;
"""

#
# Open a connection to the Sierra database and run the SQL query
#
conn = psycopg2.connect(host=db_host, port=port, database=sierra_database, user=sierra_user, password=sierra_user_password)
cur = conn.cursor()
cur.execute(sql_query)
result_set = cur.fetchall()
column_names = [desc[0] for desc in cur.description]
conn.close()
rows = result_set.__len__()
s = 's'
if (rows == 1):
    s = ''
if (rows > 0):
    print('SQL query produced ' + str(rows) + ' row' + s)
    # Tabular results are much more readable using pprint() compared to print()
    print(column_names)
    pprint(result_set)
    # Leave the two previous lines uncommented until you're satisfied with the query output
else:
    # No work to do today
    exit()
#
# Print the query results
#
CODE = 0
NAME = 1
divider = '----------------------------------------\n\t'
row = 0
while row < rows:
    print(divider + result_set[row][CODE] + '   ' + result_set[row][NAME])
    divider = '\t'
    row += 1
exit()
