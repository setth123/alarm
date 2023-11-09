import sqlite3
from tasksdb import *
def init():
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (hour INTEGER,minute INTEGER,type VARCHAR(3),reps INTEGER,sound VARCHAR(50),active INTERGER)''')
    connection.commit()
    connection.close()

def add(time,reps,sound,active):
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''INSERT INTO users (hour,minute,type,reps,sound,active) VALUES(?,?,?,?,?,?)''',(time[0],time[1],time[2],reps,sound,active))
    connection.commit()
    connection.close()
    t_add(time[0],time[1],time[2],active)

def show():
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM users''')
    records=cursor.fetchall()
    connection.commit()
    connection.close()
    return records

def dele(hour,minute,type):
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''DELETE FROM users WHERE hour = ? AND minute= ? AND type= ?''',(hour,minute,type))
    connection.commit()
    connection.close()
    t_dele(hour,minute,type)
def alter(time, reps, sound, ohour, ominute,otype):
    connection = sqlite3.connect('localdb.db')
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET hour=?, minute=?, type=?, reps=?, sound=? WHERE hour=? AND minute=? AND type=?''', (time[0], time[1], time[2], reps, sound, ohour, ominute,otype))
    connection.commit()
    connection.close()
    t_alter(time[0],time[1],time[2],ohour,ominute,otype)

def turn(state,curhour,curmin,type):
    connection = sqlite3.connect('localdb.db')
    cursor = connection.cursor()
    cursor.execute('''UPDATE users SET active=? WHERE hour=? AND minute=? AND type=?''', (state, curhour, curmin,type))
    connection.commit()
    connection.close()
    switch(state,curhour,curmin,type)