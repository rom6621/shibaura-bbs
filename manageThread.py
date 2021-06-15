#################################################
# Designer :
# Date :
# Purpose :
#################################################

#################################################
# Function Name :
# Designer :
# Date :
# Function:
# Return :
#################################################

import sqlite3


def Thread_Registration(threadName, tagName):

    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    sql = 'INSERT INTO thread (threadName, tagName) values ("' + \
        threadName + '","' + tagName + '")'
    cur.execute(sql)

    sql = 'SELECT threadID FROM thread ORDER BY threadID DESC LIMIT 1'

    cur.execute(sql)

    threadID = cur.fetchall[0]

    cur.close()
    conn.close()

    return threadID
