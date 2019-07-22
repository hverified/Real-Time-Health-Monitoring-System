import sqlite3

conn = sqlite3.connect('login.db')
c = conn.cursor()
text = 'sample'
def createTable():
    c.execute('CREATE TABLE IF NOT EXISTS login(Username TEXT, Password TEXT, Email TEXT)')
    result = c.execute("SELECT * FROM login WHERE Username = ?",(text))
    if len(result.fetchall())>0:
        print("user exists")
    else:
        print("user do not exist")

    conn.commit()
    c.close()
    conn.close()
createTable()
