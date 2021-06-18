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


#################################################
# Function Name :search
# Designer :
# Date :
# Function:
# Return :
#################################################


def search(searchKeys):
    searchWords = searchKeys[0]
    searchTags = searchKeys[1]

    conn = sqlite3.connect("tes")
    cur = conn.cursor()

    sql = 'SELECT * FROM Thread'
    if (len(searchWords) != 0) or (len(searchTags) != 0):
        sql += ' WHERE'
        if len(searchWords) != 0:
            sql += ' name in ('
            for searchWord in searchWords:
                sql += ('"' + searchWord + '", ')
            sql.pop()
            sql += ')'
            if len(searchTags) != 0:
                sql += ' OR'
        if len(searchTags) != 0:
            sql += ' name in ('
            for searchTag in searchTags:
                sql += ('"' + searchTag + '", ')
            sql.pop()
            sql += ')'

    cur.execute(sql)

    searchKey = cur.fetchall[0]

    cur.close()
    conn.close()

    return searchKey
