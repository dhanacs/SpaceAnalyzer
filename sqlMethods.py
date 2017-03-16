import sqlite3

# Save the data in DB
def saveToDB(uid, names, types, sizes, paths):
    # Create user id list for insertion into table
    uids = []
    uid = str(uid)
    for i in range(1, len(names) + 1):
        uids.append(uid)
    rows = sorted(zip(types, sizes, names, paths, uids))

    try:
        connection = sqlite3.connect('fileInfo.db')
        cursor = connection.cursor()

        # Create the table only once
        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'FILES';")
        if len(cursor.fetchall()) == 0:
            connection.execute('CREATE TABLE FILES (id TEXT, name TEXT, type TEXT, size TEXT, path TEXT);')
            connection.commit()
            print("====Table Created====")

        # Delete older records for this user
        cursor.execute("SELECT id FROM FILES WHERE id = '" + uid + "'")
        if len(cursor.fetchall()) > 0:
            cursor.execute("DELETE FROM FILES WHERE id = '" + uid + "'")
            connection.commit()

        for type, size, name, path, uid in rows:
            cursor.execute("INSERT INTO FILES (id,name,type,size,path) VALUES(?, ?, ?, ?, ?)", (uid, name, type, str(size), path))

        connection.commit()
        print("====Data saved to DB====")
        print("========================")
        connection.close()
        return
    except:
        connection.rollback()
        print("===Error saving to DB===")
        print("========================")
        return

# Retrieve the data from DB
# Called from list files
def retrieveFromDB(uid, types, sizes, names):
    uid = str(uid)

    try:
        connection = sqlite3.connect("fileInfo.db")
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = "SELECT type, size, name FROM FILES"
        query = query + " WHERE id = '" + uid + "'"
        query = query + " ORDER BY type DESC, size DESC;"
        cursor.execute(query)
        rows = cursor.fetchall();

        for row in rows:
            types.append(row["type"])
            names.append(row["name"])
            sizes.append(int(row["size"]))

        print("====Data retrieved from DB====")
        print("==============================")
        connection.close()
        return
    except:
        print("====Error retrieving from DB====")
        print("================================")
        return

# Retrieve the data from DB
# Called from search
def searchInDB(uid, paths, sizes, keyWord = "*"):
    uid = str(uid)

    try:
        connection = sqlite3.connect("fileInfo.db")
        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()
        query = "SELECT path, size FROM FILES WHERE path LIKE '%" + keyWord + "%'"
        query = query + " AND id = '" + uid + "'"
        query = query + " ORDER BY size DESC;"
        cursor.execute(query)
        rows = cursor.fetchall();

        for row in rows:
            paths.append(row["path"])
            sizes.append(int(row["size"]))

        print("====DB Search Success====")
        print("=========================")
        connection.close()
        return
    except:
        print("====DB Search Failed====")
        print("========================")
        return