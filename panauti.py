import sqlite3
import matplotlib.pyplot as plt
from dateutil import parser
from matplotlib import style
import matplotlib.animation as animation
from login.Ui_Dialog import logincheck

conn = sqlite3.connect('login.db')
c = conn.cursor()
#style.use('fivethirtyeight')
username = username
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    c.execute("SELECT * FROM "+username)

    rows = c.fetchall()

    #print(rows)

    temp = []
    timestamp = []
    timestamp_s = []
    emg = []
    
    for row in rows:
        temp.append(row[1])
        timestamp_s.append(row[0])
        emg.append(row[2])

    
    for time in timestamp_s:
        timestamp.append(parser.parse(time))
        
    print(temp, timestamp, emg)
    ax1.clear()
    ax1.plot(timestamp, temp)

    conn.commit()

if __name__ == "__main__":
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

