import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



conn = sqlite3.connect('datatype.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_datatype \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('datatype.db')

with conn:
    cur = conn.cursor()
    txtList = []
    for i in fileList:
        if i.endswith('.txt'):
            txtList.append(i)
    for i in txtList:
        cur.execute("INSERT INTO tbl_data(col_datatype) VALUES(?)", \
            (i,))
        print(i)
    conn.commit()
conn.close()
