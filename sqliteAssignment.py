
import sqlite3


fileList = ['information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']

conn = sqlite3.connect('sqliteAssignment.db')

with conn:
    cur = conn.cursor()
    #creates database if not already created
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT \
        )")
    conn.commit()
    #insert files with .txt extension into database
    """
    for file in fileList:
        if ".txt" in file:
            fileName = file
            cur.execute("INSERT INTO tbl_txtfiles(col_fileName) VALUES('{}')".format(file))
            conn.commit()
    """
    #prints out file names that are in database
    cur.execute("SELECT col_fileName FROM tbl_txtfiles ")
    varFiles = cur.fetchall()
    print("The files that end in a .txt extention at: \n")
    for item in varFiles:
        msg = "   {}\n".format(item[0])
        print(msg)
    
conn.close()
