import sqlite3
from datetime import datetime
from taskschedule import *
def t_init():
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (name VARCHAR(30),start_day VARCHAR(20),enable BOOLEAN )''')
    connection.commit()
    connection.close()
def t_add(hour,minute,type,active):
    t_init()
    name=str(hour)+":"+str(minute)+type
    if(type=="PM"):
        if(hour==12):
            hour==0
        hour+=12
    hours=str(hour).zfill(2)
    minutes=str(minute).zfill(2)
    now=datetime.now()
    start_day=str(now.date())+"T"+hours+":"+minutes+":00"
    enable=active
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''INSERT INTO tasks (name,start_day,enable) VALUES(?,?,?)''',(name,start_day,enable))
    connection.commit()
    connection.close()
def t_show():
    t_init()
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''SELECT * FROM tasks''')
    records=cursor.fetchall()
    connection.commit()
    connection.close()
    return records
def t_dele(hour,minute,type):
    name=str(hour)+":"+str(minute)+type
    connection=sqlite3.connect('localdb.db')
    cursor=connection.cursor()
    cursor.execute('''DELETE FROM tasks WHERE name = ?''',(name))
    connection.commit()
    connection.close()
    dele(name)
def t_alter(hour,minute,type,o_hour,o_minute):
    new_name=str(hour)+":"+str(minute)+type
    if(type=="PM"):
        if(hour==12):
            hour==0
        hour+=12
    hours=str(hour).zfill(2)
    minutes=str(minute).zfill(2)
    now=datetime.now()
    new_start_day=str(now.date())+"T"+hours+":"+minutes+":00"
    old_name=str(o_hour)+":"+str(o_minute)+type
    connection = sqlite3.connect('localdb.db')
    cursor = connection.cursor()
    cursor.execute('''UPDATE tasks SET name=?,start_day=? WHERE name=old_name''', (new_name, new_start_day))
    connection.commit()
    connection.close()
    alter(new_name,new_start_day,old_name)
def switch(active,curhour,curmin,type):
    name=str(curhour)+":"+str(curmin)+type
    connection = sqlite3.connect('localdb.db')
    cursor = connection.cursor()
    cursor.execute('''UPDATE tasks SET enable=? WHERE name=?''', (active,name))
    connection.commit()
    connection.close()
    toggle(active,name)